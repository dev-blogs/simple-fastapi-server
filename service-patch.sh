kubectl patch service uvicorn-app -p '{"spec":{"selector":{"app":"uvicorn-app","version":"green"}}}'
