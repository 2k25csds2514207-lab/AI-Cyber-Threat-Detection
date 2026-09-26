import pandas as pd
from io import StringIO


def test_raw_data_loading():
    raw_data = """src_ip,dst_ip,bytes
192.168.1.1,10.0.0.1,100
192.168.1.2,10.0.0.2,200
"""

    df = pd.read_csv(StringIO(raw_data))

    assert not df.empty
    assert len(df) == 2
    assert "src_ip" in df.columns
    assert "dst_ip" in df.columns
    assert "bytes" in df.columns


def test_empty_raw_data():
    raw_data = """src_ip,dst_ip,bytes
"""

    df = pd.read_csv(StringIO(raw_data))

    assert df.empty


def test_missing_values():
    raw_data = """src_ip,dst_ip,bytes
192.168.1.1,,100
"""

    df = pd.read_csv(StringIO(raw_data))

    assert df.isnull().any().any()


def test_duplicate_rows():
    raw_data = """src_ip,dst_ip,bytes
192.168.1.1,10.0.0.1,100
192.168.1.1,10.0.0.1,100
"""

    df = pd.read_csv(StringIO(raw_data))

    assert df.duplicated().any()
