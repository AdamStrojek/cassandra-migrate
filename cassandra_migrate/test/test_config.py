from unittest import mock

from cassandra_migrate import MigrationConfig


def test_create_config_object_with_sample_data():
    data = {
        'keyspace': 'test',
        'migrations_path': 'migrations',
    }
    config = MigrationConfig(data, '/test_base_path')
    assert config.keyspace == 'test'
    assert config.migrations_path == '/test_base_path/migrations'


@mock.patch.dict('os.environ', CASSANDRA_KEYSPACE='test_value', CASSANDRA_MIGRATIONS_PATH='test_path')
def test_create_config_with_variables_in_values():
    data = {
        'keyspace': '$CASSANDRA_KEYSPACE',
        'migrations_path': '$CASSANDRA_MIGRATIONS_PATH',
    }
    config = MigrationConfig(data, '/test_base_path')
    assert config.keyspace == 'test_value'
    assert config.migrations_path == '/test_base_path/test_path'
