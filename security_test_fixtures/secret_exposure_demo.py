"""Intentionally invalid secret-like values for scanner testing only.

None of these values are active credentials. This file must never be imported,
executed, or used by the application. It exists to exercise secret-detection
rules in the SAST test workflow.
"""

# AWS examples (the values below are public documentation-style placeholders).
AWS_ACCESS_KEY_ID = "AKIAIOSFODNN7EXAMPLE"
AWS_SECRET_ACCESS_KEY = "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY"
AWS_SESSION_TOKEN = "EXAMPLE_AWS_SESSION_TOKEN_NOT_VALID"

# Microsoft Azure examples.
AZURE_CLIENT_ID = "00000000-0000-0000-0000-000000000000"
AZURE_CLIENT_SECRET = "not-a-real-azure-client-secret"
AZURE_TENANT_ID = "11111111-1111-1111-1111-111111111111"
AZURE_STORAGE_CONNECTION_STRING = (
    "DefaultEndpointsProtocol=https;AccountName=exampleaccount;"
    "AccountKey=NOT_A_REAL_AZURE_STORAGE_KEY;EndpointSuffix=core.windows.net"
)

# Google Cloud examples.
GOOGLE_API_KEY = "AIzaSyDUMMY_KEY_FOR_SAST_TESTING_ONLY"
GCP_SERVICE_ACCOUNT = {
    "type": "service_account",
    "project_id": "example-project",
    "private_key_id": "not-a-real-private-key-id",
    "private_key": "-----BEGIN PRIVATE KEY-----\nNOT_A_REAL_KEY\n-----END PRIVATE KEY-----\n",
    "client_email": "scanner-test@example-project.iam.gserviceaccount.com",
}

# Source-control and package-registry examples.
GITHUB_TOKEN = "ghp_000000000000000000000000000000000000"
GITLAB_TOKEN = "glpat-00000000000000000000"
NPM_TOKEN = "npm_000000000000000000000000000000000000"

# Common SaaS and messaging examples.
SLACK_BOT_TOKEN = "xoxb-000000000000-000000000000-000000000000-EXAMPLE"
SLACK_WEBHOOK_URL = "https://hooks.slack.com/services/TEST/ONLY/NOT_A_REAL_WEBHOOK"
STRIPE_SECRET_KEY = "sk_test_not_a_real_stripe_key"
SENDGRID_API_KEY = "SG.not_a_real_sendgrid_key.not_a_real_signature"
TWILIO_ACCOUNT_SID = "AC00000000000000000000000000000000"
TWILIO_AUTH_TOKEN = "00000000000000000000000000000000"

# Application and database examples.
OPENAI_API_KEY = "sk-test-not-a-real-openai-key"
JWT_SIGNING_SECRET = "not-a-real-jwt-signing-secret"
DATABASE_URL = "postgresql://scanner_test:not_a_real_password@db.example.invalid:5432/testdb"
REDIS_URL = "redis://:not_a_real_password@redis.example.invalid:6379/0"
MONGODB_URI = "mongodb+srv://scanner_test:not_a_real_password@cluster.example.invalid/test"

# PEM-like material, intentionally incomplete and non-functional.
DEMO_PRIVATE_KEY = """-----BEGIN RSA PRIVATE KEY-----
THIS_IS_NOT_A_REAL_PRIVATE_KEY
-----END RSA PRIVATE KEY-----"""
