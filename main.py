import typer
from generator import Dockergen
import os
import questionary
from utils import copy_other_files, resource_path

app = typer.Typer()


@app.command()
def generate():
    template_dir = resource_path("templates")
    dockergen = Dockergen()
    config = dockergen.load_config()

    templates = [
        list
        for list in os.listdir(template_dir)
        if os.path.isdir(os.path.join(template_dir, list))
    ]

    if not templates:
        print(f"There is not template in {template_dir}")
        exit(1)

    choice = questionary.select("Choose you stack: ", choices=templates).ask()

    # copy config file
    template_dir = resource_path(f"templates/{choice}")
    current_dir = os.getcwd()
    copy_other_files(template_dir, current_dir)

    docker_config = [
        {
            "filename": "Dockerfile",
            "path": f"{choice}/Dockerfile.j2",
            "config": "dockerfile",
        },
        {
            "filename": "docker-compose.yml",
            "path": f"{choice}/docker-compose.yml.j2",
            "config": "compose",
        },
    ]

    for config_file in docker_config:
        file = dockergen.render_template(
            config_file["path"], config[choice][config_file["config"]]
        )

        with open(config_file["filename"], "w") as f:
            f.write(file)

    typer.echo(
        f"Files generated: Dockerfile & docker-compose.yml with {choice} template"
    )


if __name__ == "__main__":
    app()
