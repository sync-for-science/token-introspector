# Token Introspector

An implementation of OAuth 2.0 Token Introspection specific to SMART on FHIR.

It take a token and attempts to use it to issue a FHIR `GET Patient` API call,
usin the result to determine whether the token is `active`. Eventually it may
offer other resoltion mechanisms (e.g. inspecting a vendor-specific JWT).

## Installation

```
pip install .
```

## Configuration

Token Introspector checks the environment for:

+ **API_SERVER**: The FHIR server where tokens should be tried.

## Running

```
flask run
```
