# Overview

Our developers have the current code of an API. You can review the API by clicking on the following link [CARTO_DevOps_test_API__v1_3.zip](https://drive.google.com/file/d/1zKeZLZjcKJpLhQ7td_kmkUfdpytQmlGo/view?usp=sharing).

# Description

We need to give, implement, and document the solution for the following problems.

- They need a common local, stable, and uniform development environment for all. They use multiple OS (mainly Linux and Mac) and had multipleproblems caused by the use of different technologies between production, CI, and local environments.
- They need a stable table on BQ. Right now, that table is updated frequently causing problems so they would like to have an exactly equal copy in another place to  avoid problems. They also would like to have a script or similar to be able to replicate themselves in the future. The table is "carto-demo-data.demo_tilesets.osm_buildings".

# Challenge 1 - Local Development Environment with Docker

This repository contains configurations and files needed to create a common and stable local development environment using Docker. By following these instructions, you'll be able to set up a development environment ready to work on the project, all while harnessing the power of GitHub and Git for collaborative development.

## Prerequisites

Make sure you have the following components installed on your system:

- [Docker](https://docs.docker.com/get-docker/)
- [GitHub](https://github.com/) Account

## Collaborative Development with Git

We leverage the collaborative capabilities of Git and GitHub to enhance our development process:

- **Version Control**: Git allows us to track changes, manage versions, and collaborate seamlessly. Each developer can work on their own branch and propose changes using pull requests.

- **Code Reviews**: GitHub provides an excellent platform for code reviews. You can easily review, comment, and discuss code changes, ensuring high code quality.

- **Issue Tracking**: GitHub's issue tracking system helps us manage and prioritize tasks, allowing for efficient project management.

- **Collaboration**: Multiple developers can collaborate on the same project simultaneously, thanks to Git's branching and merging capabilities.

## Configuration

1. Clone this repository to your local development machine:

   ```bash
   git clone <repository URL>
   ```

2. Navigate to the repository directory:

   ```bash
   cd <directory name>
   ```

## Usage

To build and run the local development environment, by creating a Docker image and running a container for your `simple-api` application, follow these steps:

1. **Build the Docker Image**:
   - Navigate to the directory where the Dockerfile is located.
   - Run the following command to build the Docker image:
     ```
     docker build -t simple-api .
     ```
     Here, `simple-api` is the name you give to your Docker image, and `.` tells Docker to use the current directory (where your Dockerfile is).

2. **Run the Docker Container**:
   - After the image is built, run the container using:
     ```
     docker run -p 3000:3000 simple-api
     docker run -e GOOGLE_APPLICATION_CREDENTIALS=./carto_creds.json -p 3000:3000 -d simple-api

     ```
   - The `-p 3000:3000` argument maps port 3000 of the container to port 3000 on your host machine, allowing you to access the application via `localhost:3000`.
   - `simple-api` is the name of your Docker image.

Make sure to replace `3000` with the actual port your application uses if it's different. The above commands assume that you are in the same directory as your Dockerfile and that your application listens on port 3000.


# Challenge 2 - BigQuery Table Copy and Update Script

This script is designed to copy a specific table from the `bq-demo-templates` workspace in BigQuery to a developer's workspace, and then update that table as necessary.

## Prerequisites

Before using this script, ensure you have the following:

1. **Python Environment:** The script is written in Python. You need to have Python installed on your machine. Python 3.6 or higher is recommended.

2. **Google Cloud SDK:** Make sure you have the Google Cloud SDK installed and configured for your environment. This script uses the BigQuery Python client library, which requires the SDK.

3. **Google Cloud Credentials:** Your environment must be authenticated with Google Cloud. Set up your Google Cloud credentials and make sure they have permissions to access BigQuery. You can do it by running this command first:
   
   ```bash
   export GOOGLE_APPLICATION_CREDENTIALS="/path/to/your/file_credentials.json"
   ```

4. **Dependencies:** The `google-cloud-bigquery` library must be installed. You can install it using pip:

    ```bash
    pip install google-cloud-bigquery
    ```

## Setup and Configuration

1. **Clone the Repository:** Clone or download the script to your local machine.

2. **Google Cloud Project ID:** You will need the Google Cloud project ID for the destination workspace (developer's workspace). This ID is a required argument when running the script.

## Usage

Run the script from the command line by passing the developer's Google Cloud project ID as an argument. For example:

```bash
python bq_stable_table_bq.py my-google-project-id
```

Replace `my-google-project-id` with the actual project ID.

## How It Works

1. **Copy Table:** The script first copies the table `carto-demo-data.demo_tilesets.osm_buildings` from the `bq-demo-templates` workspace to the specified developer's workspace in BigQuery.

2. **Update Table:** After copying, the script calls an `update_table` function. This function is a placeholder and should be implemented with the specific logic for updating the table in the developer's workspace.

## Customization

- The `update_table` function needs to be customized according to the specific requirements for updating the table. This can involve running specific SQL queries, modifying the data, etc.

## Notes

- Ensure the Google Cloud credentials used for running the script have the necessary permissions to read from the source table and write to the destination project in BigQuery.
- The script provides basic functionality and error handling, logging, and more advanced features can be added as per the requirements.