# Security Policy

## Reporting a vulnerability

Do not report suspected security vulnerabilities in a public issue, discussion, or pull request.

Use GitHub's private vulnerability reporting feature if it is enabled for this repository:

`Security → Advisories → Report a vulnerability`

If private reporting is unavailable, contact the repository owner privately using the contact method listed on the VERIQTA GitHub profile. Do not include secrets or exploit details in a public message.

Please include:

- The affected file, example, workflow, or dependency
- A clear description of the issue and its possible impact
- Steps to reproduce or a minimal proof of concept
- Any known affected versions or environments
- A suggested remediation, if available

## What to expect

The maintainer will assess the report, request clarification if needed, and decide whether repository content or dependencies require correction. Please allow time for investigation before sharing details publicly.

This is an educational repository, so it may not publish versioned software releases. Security reports about unsafe instructions, exposed credentials, vulnerable workflows, malicious links, or risky dependency examples are still welcome.

## Accidental secret exposure

If you find a token, password, private key, connection string, personal record, or other sensitive value:

1. Do not use, copy, test, or redistribute it.
2. Report its exact location privately.
3. Do not open a public issue or pull request containing the value.

Repository history may retain deleted secrets. The owner should revoke or rotate the credential before removing it from current files and history.

## Supported content

Security fixes are applied to the current default branch. Old forks, copied snippets, archived branches, and external resources are outside the project's control.

## Safe-harbor intent

Good-faith reports that avoid privacy violations, service disruption, data destruction, and unauthorized access are welcomed. This statement does not authorize testing of third-party systems, cloud accounts, or services referenced by the repository.
