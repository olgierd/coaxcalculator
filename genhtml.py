#!/usr/bin/env python3

import jinja2
import json
import os
import sys
import yaml


def generate_html():
    current_dir = os.getcwd()

    with open(os.path.join(current_dir, 'cables.yaml'), 'r') as cable_yaml_file:
        cable_data_json = json.dumps(yaml.safe_load(cable_yaml_file))

    with open(os.path.join(current_dir, 'index.html.j2'), 'r') as template_file:
        rendered = jinja2.Template(template_file.read()).render(cable_json=cable_data_json)

    with open(os.path.join(current_dir, 'docs/index.html'), 'w') as output_html:
        output_html.write(rendered)


if __name__ == '__main__':
    generate_html()