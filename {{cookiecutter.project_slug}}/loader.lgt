% Loader for {{ cookiecutter.project_name }}

:- initialization((
	logtalk_load([ % Dependencies
	]),
	logtalk_load([ % Application
		{{ cookiecutter.project_slug }}
	], [
	  % optimize(on)
	])
)).
