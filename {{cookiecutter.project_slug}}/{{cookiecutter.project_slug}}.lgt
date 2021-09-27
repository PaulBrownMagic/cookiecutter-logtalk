:- object({{ cookiecutter.project_slug }}).

	:- info([
		version is 0:1:0,
		author is '{{ cookiecutter.author }}',
		date is {{ cookiecutter.date }},
		comment is '{{ cookiecutter.project_name }}'
	]).

:- end_object.
