# Unit Testing with Pytest for Data Receiver Implementation

This repository contains a Python project focused on unit testing using Pytest for a data receiver implementation.

## Table of Contents

1. [Overview](#overview)
2. [Project Structure](#project-structure)
3. [Implementation Details](#implementation-details)
    - [DataReceiver Class](#datareceiver-class)
4. [Unit Tests](#unit-tests)
    - [test_data_receiver.py](#test_data_receiverpy)

## Overview

The project demonstrates unit testing techniques using Pytest for a data receiver implementation. The `DataReceiver` class is tested to ensure that data validation, cleanup, and storage functionalities work correctly.

## Project Structure

The project structure is organized as follows:

- `src/`
  - `data_receiver.py`: Contains the `DataReceiver` class implementation for data validation, cleanup, and storage.

- `tests/`
  - `test_data_receiver.py`: Pytest scripts to test various aspects of the `DataReceiver` class.

## Implementation Details

### DataReceiver Class

The `DataReceiver` class in `data_receiver.py` implements methods to validate, clean up, and store data.

#### Methods:

- `__init__(self, dataset_id, table_id)`: Constructor initializes with dataset and table identifiers.
- `check_validity(self, data)`: Validates incoming data.
- `clean_up_data(self, _data)`: Removes unnecessary fields from the data.
- `write(self, client, data)`: Writes cleaned data to storage.

## Unit Tests

### `test_data_receiver.py`

Unit tests in this file validate the functionality of the `DataReceiver` class using Pytest.

- `test_check_validity()`: Validates data to ensure required fields are present.
- `test_check_validity_with_exception()`: Tests validation with expected exceptions.
- `test_cleanup_data()`: Ensures data cleanup removes unnecessary fields.
- `test_write()`: Mocks external dependencies to test data storage functionality.