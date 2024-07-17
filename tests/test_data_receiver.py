import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))
import pytest
from data_receiver import DataReceiver
from unittest.mock import Mock

def test_check_validity():
    data = {
        "important": "12345"
    }
    service = DataReceiver(None,None)
    service.check_validity(data)

def test_check_validity_with_exception():
    data = {
        "temp": "12345"
    }
    service = DataReceiver(None,None)
    with pytest.raises(AssertionError) as e:
        service.check_validity(data)

    assert str(e.value) == "FAILED"

def test_cleanup_data():
    _data = {
        "important": "12345",
        "not_needed": "678",
        "temp": "9101112"
    }
    service = DataReceiver(None,None)
    data = service.clean_up_data(_data)
    assert len(data.items()) == 1
    assert "temp" not in data
    assert "not_needed" not in data

    assert len(_data.items()) == 3
    assert "temp" in _data
    assert "not_needed" in _data

# dealing with external dependency with mock
def test_write():
    data = {
        "important": "12345",
    }
    mock = Mock()
    mock.insert_rows_json.return_value = []
    service = DataReceiver(None, None)
    errors = service.write(mock, data)

    assert not errors