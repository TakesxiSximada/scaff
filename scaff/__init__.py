#! /usr/bin/env python
# -*- coding: utf-8 -*-
import os
import sys
import copy
import argparse
import itertools
from collections import OrderedDict

import mako.lookup
import scaff


DEFAULT_TEMPLATE_DIR = os.path.join(
    os.path.abspath(os.path.dirname(scaff.__file__)),
    'templates')

DEFAULT_EXTRA_TEMPLATE_DIR = os.path.join(
    os.path.abspath(os.path.dirname(scaff.__file__)),
    'extra_templates')


class Scaffolder(object):
    'SCAFF_TEMPLATE'
    general_contexts = OrderedDict((
        ('package', None),
        ('version', None),
        ('description', None),
        ('web', None),
        ('repository', None),
        ('download', None),
        ('bts', None),
        ('vcs', None),
        ('name', None),
        ('email', None),
        ))
    special_contexts = OrderedDict((
        ('.gitignore', {}),
        ('README.rst', {}),
        ('setup.cfg', {}),
        ('setup.py', {}),
        ('index.html', {}),
        ('bower.json', {}),
        ('gulpfile.js', {}),
        ('package.json', {}),
        ('doc/index.html', {}),
        ))

    def get_custom_template_dirs(self):
        return os.environ.get('SCAFF_TEMPLATE', '').split(':')

    def get_contexts(self, contexts_template):
        contexts = {}
        for key, value in contexts_template.items():
            prompt = '{} '.format(key)
            if value:
                prompt + '(defaut: {})'.format(value)
            prompt += ': '

            while True:
                val = input(prompt).strip()
                contexts[key] = val or value
                if contexts[key]:
                    break
        return contexts

    def scaffolding(self, target_dir, typ):
        if not os.path.isdir(target_dir):
            os.makedirs(target_dir)
        os.chdir(target_dir)

        custom_template_dirs = self.get_custom_template_dirs()
        template_dirs = custom_template_dirs if custom_template_dirs else []
        template_dirs.append(DEFAULT_TEMPLATE_DIR)
        template_dirs = [os.path.join(dirpath, typ) for dirpath in template_dirs]

        lookupper = mako.lookup.TemplateLookup(
            directories=template_dirs,
            input_encoding='utf-8',
            output_encoding='utf-8',
            encoding_errors='replace',
            )

        general_contexts = self.get_contexts(self.general_contexts)

        cur = os.getcwd()
        for recipe in self.special_contexts.keys():
            print('---> {}'.format(recipe))

            special_contexts = self.special_contexts[recipe]
            tmpl = lookupper.get_template(recipe)
            output_path = os.path.join(cur, recipe)

            output_dir = os.path.dirname(output_path)
            if not os.path.isdir(output_dir):
                os.makedirs(output_dir)

            contexts = copy.deepcopy(general_contexts)
            custom_contexts = self.get_contexts(special_contexts)
            contexts.update(custom_contexts)

            buf = tmpl.render(**contexts)
            with open(output_path, 'w+b') as fp:
                fp.write(buf)

        # namespace_package for python
        package = general_contexts['package']
        namespace = package.split('.')
        namespace[0] = os.path.join('src', namespace[0])
        tmpl = lookupper.get_template('src/namespace/__init__.py')
        buf = tmpl.render()
        for path in itertools.accumulate(namespace, func=os.path.join):
            os.makedirs(path)
            with open(os.path.join(path, '__init__.py'), 'w+b') as fp:
                fp.write(buf)
        tmpl = lookupper.get_template('src/namespace/package/__init__.py')
        buf = tmpl.render()
        path = os.path.join('/'.join(namespace), '__init__.py')
        with open(path, 'w+b') as fp:
            fp.write(buf)

def main(argv=sys.argv[1:]):
    parser = argparse.ArgumentParser()
    parser.add_argument('-t', '--type', dest='typ', default='python')
    parser.add_argument('-d', '--directory', default=os.getcwd())
    opts = parser.parse_args(argv)

    scaffolder = Scaffolder()
    scaffolder.scaffolding(opts.directory, opts.typ)

if __name__ == '__main__':
    main()
