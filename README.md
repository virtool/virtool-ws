# virtool-ws

Websocket service which reads API response objects sent from 
Virtool over a Redis Pub/Sub channel and sends them to all connected clients. 

## Getting Started 

Dependencies & virtual environments are managed with [Poetry](https://python-poetry.org).

Poetry can be installed by following the
[official installation guide](https://python-poetry.org/docs/master/#installing-with-the-official-installer).

To install dependencies and `virtool-ws` install a virtual environment, clone the repository and run:

```shell
poetry install
```

The service can be started up using the following command:

```sh
poetry run python run.py 
```

## Contributing

### Tests

[Pytest](https://docs.pytest.org) is used to implement unit and 
integration tests.

The test suite requires Redis to be running and configured. 
See the [Virtool compose repository](https://github.com/virtool/compose) 
for a predefined configuration that can be used for developing Virtool services.

To run the entire test suite:

```sh
poetry run pytest
```

### Commits

All commits must follow the [Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0) specification.

These standardized commit messages are used to automatically publish releases using [`semantic-release`](https://semantic-release.gitbook.io/semantic-release)
after commits are merged to `main` from successful PRs.

**Example**

```text
feat: add API support for assigning labels to existing samples
```

Descriptive bodies and footers are required where necessary to describe the impact of the commit. Use bullets where appropriate.

Additional Requirements

1. **Write in the imperative**. For example, _"fix bug"_, not _"fixed bug"_ or _"fixes bug"_.
2. **Don't refer to issues or code reviews**. For example, don't write something like this: _"make style changes requested in review"_.
   Instead, _"update styles to improve accessibility"_.
3. **Commits are not your personal journal**. For example, don't write something like this: _"got server running again"_
   or _"oops. fixed my code smell"_.

From Tim Pope: [A Note About Git Commit Messages](https://tbaggery.com/2008/04/19/a-note-about-git-commit-messages.html)


