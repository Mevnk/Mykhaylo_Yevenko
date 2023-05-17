import dropbox
import pytest


class DropboxClientFactory:
    def __init__(self, access_token):
        self.access_token = access_token

    def create_client(self):
        return dropbox.Dropbox(self.access_token)


class TestDropboxAPI:
    @pytest.fixture
    def dropbox_client(self, request):
        access_token = request.config.getoption("--access-token")
        factory = DropboxClientFactory(access_token)
        return factory.create_client()

    def test_upload_file(self, dropbox_client):
        # Upload a test file to Dropbox
        file_path = 'file.txt'
        dropbox_path = '/file.txt'

        with open(file_path, 'rb') as f:
            response = dropbox_client.files_upload(f.read(), dropbox_path)

    def test_get_file_metadata(self, dropbox_client):
        # Get metadata for a test file in Dropbox
        file_path = '/file.txt'

        response = dropbox_client.files_get_metadata(file_path)

        # Assert that the metadata retrieval was successful
        assert response.name == 'file.txt'

    def test_delete_file(self, dropbox_client):
        # Delete a test file from Dropbox
        file_name = 'file.txt'
        file_path = '/' + file_name
        response = dropbox_client.files_delete(file_path)

        # Assert that the file deletion was successful
        folder_contents = dropbox_client.files_list_folder("").entries
        file_exists = any(entry.name == file_name for entry in folder_contents)
        assert not file_exists


# Generate a report after the tests are run
def pytest_terminal_summary(terminalreporter):
    passed = len(terminalreporter.stats.get('passed', []))
    failed = len(terminalreporter.stats.get('failed', []))

    print("\n--- Dropbox API Test Summary ---")
    print(f"Passed: {passed}")
    print(f"Failed: {failed}")

