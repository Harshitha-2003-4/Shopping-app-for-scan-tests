"""Intentionally insecure SAST test fixture.

This module exists only to verify that the AccuKnox OpenGrep workflow reports
findings. Do not import, execute, deploy, or copy these examples into
application code. All values below are non-functional test data.
"""

import hashlib
import os
import pickle
import random
import sqlite3
import ssl
import subprocess
import tempfile

import requests
import yaml


# Non-functional placeholder values used solely to exercise secret detectors.
DEMO_PASSWORD = "not-a-real-password-for-sast-testing"
DEMO_API_KEY = "demo_api_key_1234567890_not_for_use"


def run_user_command(command):
    """SAST should flag shell execution with untrusted input."""
    return subprocess.run(command, shell=True, check=False)


def build_sql_query(username):
    """SAST should flag string-formatted SQL."""
    connection = sqlite3.connect(":memory:")
    return connection.execute("SELECT * FROM users WHERE name = '%s'" % username)


def deserialize_untrusted_data(payload):
    """SAST should flag unsafe deserialization."""
    return pickle.loads(payload)


def parse_untrusted_yaml(content):
    """SAST should flag unsafe YAML loading."""
    return yaml.load(content)


def download_without_tls_validation(url):
    """SAST should flag disabled TLS certificate verification."""
    return requests.get(url, verify=False, timeout=5)


def insecure_hashes(value):
    """SAST should flag weak cryptographic hash functions."""
    return hashlib.md5(value).hexdigest(), hashlib.sha1(value).hexdigest()


def generate_predictable_token():
    """SAST should flag a non-cryptographic random value used as a token."""
    return str(random.random())


def create_insecure_temp_file():
    """SAST should flag the race-prone tempfile API."""
    return tempfile.mktemp()


def disable_certificate_checks():
    """SAST should flag creation of an unverified TLS context."""
    return ssl._create_unverified_context()


def execute_os_command(command):
    """SAST should flag direct operating-system command execution."""
    return os.system(command)
