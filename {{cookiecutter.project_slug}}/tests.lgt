:- object(tests,
	extends(lgtunit)).

	:- info([
		version is 1:0:0,
		author is '{{ cookiecutter.author }}',
		date is {{ cookiecutter.date }},
		comment is 'Unit tests for {{ cookiecutter.project_name }}'
	]).

	cover({{ cookiecutter.project_slug }}).

	test({{ cookiecutter.project_slug }}_exists, true) :-
		current_object({{ cookiecutter.project_slug}}).

:- end_object.
