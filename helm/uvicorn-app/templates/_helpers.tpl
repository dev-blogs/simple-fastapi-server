{{- define "uvicorn-app.name" -}}
uvicorn-app
{{- end }}

{{- define "uvicorn-app.fullname" -}}
{{ include "uvicorn-app.name" . }}
{{- end }}
