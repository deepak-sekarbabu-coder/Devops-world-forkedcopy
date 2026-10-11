# Contributing to DEVOPS-WORLD

Thank you for helping improve DEVOPS-WORLD. This guide explains what the project accepts and how to prepare a contribution that can be reviewed efficiently.

## Before you contribute

- Read this guide and the [Code of Conduct](CODE_OF_CONDUCT.md).
- Search existing issues and pull requests to avoid duplicate work.
- Open an issue before making a large structural change, adding a major learning path, or rewriting an established section.
- Keep each pull request focused on one topic or closely related set of changes.
- Use your own work or material you have permission to contribute.

## Contributions we welcome

- Corrections to technical errors
- Repairs for broken or outdated links
- Clearer explanations and useful examples
- Reproducible labs and production-style projects
- Troubleshooting scenarios with evidence-based diagnosis
- Security improvements and safer defaults
- Architecture or workflow diagrams
- Current official documentation and reputable references
- Accessibility, navigation, grammar, and formatting improvements

## Contributions we do not accept

- Exam dumps, leaked questions, or material that violates certification rules
- Copyrighted or copied material without permission and attribution
- Promotional spam, affiliate-link collections, or undisclosed advertising
- Secrets, credentials, personal data, or real production information
- Commands that are destructive without prominent warnings and safeguards
- Unverified instructions presented as tested
- Low-effort, generic, or unreviewed AI-generated content
- Duplicate resources that add no new educational value
- Changes unrelated to DevOps or modern infrastructure engineering

## Quality standard

Every technical contribution should be:

1. Accurate. Check commands, terminology, and claims.
2. Reproducible. State prerequisites, versions, and required permissions.
3. Safe. Use least privilege, protect secrets, and explain destructive steps.
4. Practical. Explain why the material matters and where it applies.
5. Observable. Include a way to verify success or diagnose failure.
6. Maintainable. Prefer stable links, current practices, and clear structure.
7. Original. Attribute sources and comply with their licenses.

## Documentation requirements

Use plain, direct language. Define specialized terms when first introduced. Prefer short sections, descriptive headings, lists, and tables where they improve scanning.

For a tutorial, project, or lab, include the relevant items below:

- Objective
- Architecture or workflow
- Prerequisites
- Tested versions and environment
- Setup steps
- Commands and configuration
- Expected output
- Verification
- Security considerations
- Cost considerations for cloud resources
- Common mistakes
- Failure scenarios and troubleshooting
- Cleanup
- References

Do not claim a lab is tested unless you ran it successfully in the stated environment.

## Commands and safety

- Explain commands that may delete data, change permissions, expose a service, or incur cost.
- Use placeholders such as `<account-id>` and `<region>` instead of real values.
- Never commit passwords, tokens, private keys, connection strings, or `.env` files.
- Prefer least-privilege examples.
- Pin versions where reproducibility or supply-chain integrity requires it.
- Include cleanup steps for resources that may continue to generate charges.

## Links and sources

- Prefer official documentation and primary sources.
- Link to the canonical page rather than a search result.
- Avoid URLs pinned to a temporary commit unless the historical version is intentional.
- Check every new link before submitting.
- Credit adapted ideas, code, diagrams, and quotations.

## Using AI-assisted tools

AI-assisted contributions are allowed only when the contributor personally reviews, tests, and takes responsibility for the result.

Do not submit generated material that contains invented commands, fabricated citations, repeated filler, unexplained code, or content you cannot verify. Mention material AI assistance in the pull request when it substantially shaped the contribution.

## Making a contribution

1. Fork the repository.
2. Create a branch from the default branch.
3. Make one focused change.
4. Test commands, links, examples, and formatting.
5. Review your diff for secrets and unrelated edits.
6. Commit with a clear message.
7. Push the branch to your fork.
8. Open a pull request using the repository template.

Example branch names:

```text
docs/fix-linux-permissions-guide
lab/add-docker-healthcheck
fix/update-kubernetes-link
```

Example commit messages:

```text
docs: clarify Linux file permissions example
fix: repair Kubernetes networking links
feat: add Docker health-check lab
```

## Pull request checklist

Before submitting, confirm that:

- The change has a clear educational or engineering purpose.
- The technical content is accurate and tested where applicable.
- No secrets, personal data, or proprietary information are included.
- Destructive commands have warnings and safeguards.
- Cloud labs include cost and cleanup guidance.
- New sources are trustworthy and properly attributed.
- Links work and images have meaningful alternative text.
- The change does not duplicate existing material.
- The pull request describes what changed, why, and how it was verified.

## Review process

Maintainers may request changes for accuracy, scope, safety, style, licensing, or maintainability. Approval is not guaranteed. A contribution may be closed if it is out of scope, inactive after requested changes, or incompatible with project standards.

Review feedback is about the contribution, not the contributor. Keep discussion specific, respectful, and evidence-based.

## Licensing and attribution

By submitting a contribution, you confirm that you have the right to provide it and agree that it may be distributed under the repository's license. Preserve required notices and attribution for third-party material.

If you are unsure whether material can be contributed, open an issue before submitting it.
