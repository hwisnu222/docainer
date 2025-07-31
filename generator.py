from jinja2 import Environment, FileSystemLoader
import yaml

from utils import resource_path


class Dockergen:
    env = Environment(loader=FileSystemLoader(resource_path("templates")))

    def render_template(self, template_name, context):
        template = self.env.get_template(template_name)
        return template.render(context)

    def load_config(self, path=resource_path("config.yaml")):
        with open(path) as file:
            return yaml.safe_load(file)
