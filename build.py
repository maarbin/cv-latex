import yaml
from jinja2 import Environment, FileSystemLoader
from pathlib import Path
import subprocess

#Custom delimiters for Jinja2 to avoid conflicts with LaTeX syntax
env = Environment(
    loader=FileSystemLoader('templates'),
    block_start_string='((*',
    block_end_string='*))',
    variable_start_string='(((',
    variable_end_string=')))',
    comment_start_string='((=',
    comment_end_string='=))',
) 

def render_cv(lang, gdpr):
    with open(f'content/{lang}.yaml', 'r', encoding='utf-8') as f:
        content = yaml.safe_load(f)

    template = env.get_template('cv_template.tex.jinja')

    rendered_tex = template.render(**content, gdpr=gdpr)

    suffix = '_gdpr' if gdpr else ''
    tex_filename = f'cv_{lang}{suffix}.tex'
    pdf_filename = tex_filename.replace('.tex', '.pdf')
    Path(tex_filename).write_text(rendered_tex, encoding='utf-8')

    subprocess.run(['pdflatex', tex_filename], check=True)

    print(f"PDF generated: {pdf_filename}")


render_cv('en', gdpr=True)
render_cv('pl', gdpr=True)
render_cv('en', gdpr=False)
render_cv('pl', gdpr=False)