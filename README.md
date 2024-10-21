# Efficient Data Stream Anomaly Detection
 
Data stream generator and anomaly detector based on EMA and Z-Score using Python.

## Table of contents

- [Installation](#installation)
- [Usage](#usage)
- [Algorithm](#algorithm)
- [Contributing](#contributing)
- [License](#license)

## Installation

To install the required libraries open the folder and run the command:
	```
	pip install -r requirements.txt
	```

If using conda, run the command:
	```
	conda create --name <env> --file requirements.txt
	```

Alternatively, only the external library matplotlib is required, so it can be installed independently.

## Usage

To start the graph, open the folder of the project and run the following command:
	```
	python main.py
	```

## Algorithm

This code uses a mix of exponential moving average and Z-Score:

- EMA is used to give more weight to more recent data on average, mitigating the seasonal behavior of the data.
- Z-Score is used to judge how deviant each data point is compared to the previous behaviors.

The anomaly_detector class does not have access to the data generation functions, so the algorithm infers any tendency in the data.

## Contributing

This was made as a technical test, but feel free to contribute as you wish:

1. Fork the repository.

2. Create a new branch for your feature or bugfix: 

	```
	git checkout -b feature-name
	```

3. Make your changes and commit them: 

	```
	git commit -m "Description of your changes"
	```

4. Push your changes to your fork: 
	
	```
	git push origin feature-name
	```

5. Open a pull request on the main repository.

## License

This project is licensed under the MIT License.
