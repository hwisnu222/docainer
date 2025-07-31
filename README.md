# Docainer

Docainer is a command-line tool that generates production-ready `Dockerfile` and `docker-compose.yml` files from predefined templates using a simple configuration file.

Currently supported on Linux only.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Configuration](#configuration)
- [Supported Stacks](#supported-stacks)
- [Generated Dockerfile Template](#generated-dockerfile-template)
- [Generated Docker Compose Template](#generated-docker-compose-template)
- [Contributing](#contributing)
- [License](#license)

## Introduction

Docainer helps developers quickly scaffold Docker configurations for web projects (e.g., Django, React, Next.js) using minimal YAML configuration. It is optimized for production environments.

## Features

- Auto-generates Dockerfile and docker-compose.yml
- Based on customizable Jinja2 templates
- Stack-aware (supports Django, React, Next.js, and more)
- Production-ready structure
- CLI-based interactive selection

## Installation

Ensure Python 3.10+ and a Linux OS.

### Option 1: Clone and Build Manually

```
git clone https://github.com/hwisnu222/docainer.git
cd docainer
make build
cd dist/
chmod +x docainer
sudo mv docainer /usr/local/bin/
```

This will produce a binary file named `docainer`.

### Option 2: Download Prebuilt Binary from Release

Download the latest release and install it globally:

```
curl -s https://raw.githubusercontent.com/hwisnu222/docainer/main/install.sh | sh
```

#### wget:

```
wget -qO - https://raw.githubusercontent.com/hwisnu222/docainer/main/install.sh | sh
```

Now you can run it from anywhere:

```
docainer
```

## Usage

To run the generator:

```
docainer
```

You will be prompted to choose a stack. The tool will then generate the corresponding Dockerfile and docker-compose.yml files in your current directory.

## Configuration

Stacks are defined in `config.yaml`. Example configuration:

```
reactjs:
  dockerfile:
    base_image: node:20-alpine
    nginx_image: nginx:stable-alpine
  compose:
    service_name: "react-app"
    port: 3000
    container_port: 80
```

You can add more stacks using the same structure.

## Supported Stacks

- Django
- ReactJS
- NextJS

You may add more by creating new folders inside the `templates/` directory.

## Generated Dockerfile Template

```
FROM {{ base_image }}

WORKDIR /app

COPY . .

RUN {{ install_command }}

CMD [ "{{ run_command }}" ]
```

## Generated Docker Compose Template

```
version: "3"

services:
  {{ service_name }}:
    build:
      context: .
      dockerfile: Dockerfile
    ports:
      - "{{ port }}:{{ container_port }}"
```

## Contributing

You are welcome to contribute by opening issues or pull requests.

## License

This project is licensed under the MIT License.
