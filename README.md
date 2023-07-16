![image](https://github.com/MuhFaridanSutariya/jakarta-pollution-classification/assets/88027268/9ec31df5-5efb-4436-b08b-7972b67dc5af)

## How to run

### 1. Clone this repository
To get started, clone this repository onto your local machine. Follow the instructions below:

1. Open a terminal or Command Prompt.
2. Change to the directory where you want to clone the repository.
3. Enter the following command to clone the repository:
   ```bash
   git clone https://github.com/MuhFaridanSutariya/jakarta-pollution-classification.git
   ```
4. Once the cloning process is complete, navigate into the cloned directory using the `cd` command:
   ```bash
   cd jakarta-pollution-classification
   ```

### 2. System Requirements
Make sure your system meets the following requirements before proceeding:
- Python 3.10+ is installed on your computer.
- Pip (Python package installer) is installed.

### 3. Create a Virtual Environment
A virtual environment will allow you to separate this project from the global Python installation. Follow these steps to create a virtual environment:

**On Windows:**
Open Command Prompt and enter the following command:
```bash
python -m venv virtualenv_name
```
Replace `virtualenv_name` with the desired name for your virtual environment.

**On macOS and Linux:**
Open the terminal and enter the following command:
```bash
python3 -m venv virtualenv_name
```
Replace `virtualenv_name` with the desired name for your virtual environment.

### 4. Activate the Virtual Environment
After creating the virtual environment, you need to activate it before installing the requirements. Use the following steps:

**On Windows:**
In Command Prompt, enter the following command:
```bash
virtualenv_name\Scripts\activate
```
Replace `virtualenv_name` with the name you provided in the previous step.

**On macOS and Linux:**
In the terminal, enter the following command:
```bash
source virtualenv_name/bin/activate.bat
```
Replace `virtualenv_name` with the name you provided in the previous step.

### 5. Install Requirements
Once the virtual environment is activated, you can install the project requirements from the `requirements.txt` file. Follow these steps:

**On Windows, macOS, and Linux:**
In the activated virtual environment, navigate to the directory where the `requirements.txt` file is located. Then, enter the following command:
```bash
pip install -r requirements.txt
```
This command will install all the required packages specified in the `requirements.txt` file

### 6. Run Streamlit and FastAPI:

Please run this command at the same time

How to run FAST API:

``uvicorn <replace-with-namefile>:app --reload``

How to run Streamlit:

``streamlit run <replace-with-namefile>``

Open your port as mentioned in terminal prompt.

### 7. API Endpoint:

`POST /predict`
Make a POST request to this endpoint to get pollution predictions.

<b>Request Body</b>

The request body should be a JSON object with the following fields:

- stasiun: str (DKI1 (Bunderan HI), DKI2 (Kelapa Gading), DKI3 (Jagakarsa), DKI4 (Lubang Buaya), DKI5 (Kebon Jeruk) Jakarta Barat)
- pm10: float (-1 - 800)
- pm25: float (-1 - 400)
- so2: float (-1 - 500)
- co: float (-1 - 100)
- o3: float (-1 - 160)
- no2: float (-1 - 100)

Example request body:
`
{
    "stasiun": DKI1 (Bunderan HI),
    "pm10": 10.5,
    "pm25": 5.2,
    "so2": 0.8,
    "co": 1.2,
    "o3": 0.4,
    "no2": 0.6
}
`

<b>Response</b>

The API will respond with a JSON object containing the prediction result:

`
{
    "status": 200,
    "input": [1.0, 0.0, 0.0, 0.0, 0.0, 10.5, 5.2, 0.8, 1.2, 0.4, 0.6],
    "message": "TIDAK SEHAT"
}
`

The `status` field indicates the status of the prediction. A value of 200 indicates a successful prediction. The `input` field shows the input values provided in the request. The `message` field contains the predicted pollution level.

In case of an error or failure, the API will respond with a status code of 204 and an error message in the `message` field.

## [OPTIONAL]
### Docker Setup and Usage

This repository provides instructions on how to build and run a Docker image. Before proceeding, ensure that Docker is installed on your Ubuntu system.

### Installation

Follow the official Docker documentation to install Docker on Ubuntu by following the step-by-step instructions provided at [https://docs.docker.com/engine/install/ubuntu/](https://docs.docker.com/engine/install/ubuntu/).

### Building the Docker Image

To build the Docker image, navigate to the directory containing the Dockerfile and run the following command:

```bash
docker build -t example_cicd .
```
Replace `example_cicd` with the desired tag name for your Docker image.

The build process will start, and Docker will execute the instructions specified in the Dockerfile to create the image.

### Running Fastapi on Docker Image
```bash
docker run -p 8009:8000 example_cicd uvicorn src.api.main:app --host 0.0.0.0
```

This command will start a container and bind port 8009 of the host machine to port 8000 of the container. The `uvicorn` command is used to run the specified Python application within the container.

You can now access the running application by opening a web browser and navigating to `http://localhost:8009`.

Note: If you want to run the container in the background (detached mode), you can add the `-d` flag to the `docker run` command.

<b>Illustration of architecture</b>


![image](https://github.com/MuhFaridanSutariya/Learn-MLProcess/assets/88027268/281fc45d-095b-49ad-bfe0-cbd74d50acc4)






