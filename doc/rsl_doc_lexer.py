'''
Created on May 25, 2017

@author: john
'''


from pygments.lexer import RegexLexer, include, words
import pygments.token as tok


import re

class RSLLexer(RegexLexer):
    name = 'pyrsl'
    aliases = ['pyrsl']
    filenames = ['*.rsl', '*.arc']

    flags = re.MULTILINE | re.IGNORECASE
    
    tokens = {
        'root': [
            (r'[\s]*\.', tok.Comment.Special, 'control'),
            (r'[\s]*\$', tok.Generic.Strong, 'substitution'),
            (r'[\s]*[^\.]', tok.Comment, 'literal'),
        ],
        'literal': [
            (r'\$', tok.Generic.Strong, 'substitution'),
            (r'[^\n]', tok.Comment),
            (r'\n', tok.Comment, '#pop'),
        ],
        'substitution': [
            (r'\{', tok.Generic.Strong),
            (r'(?i)R[0-9]+', tok.Number),
            (words(('selected',), prefix=r'\b', suffix=r'\b'),tok.Keyword),
            (r'(?i)[a-z_?][a-z_?0-9]*', tok.Name),
            (r'\->', tok.Operator, 'class'),
            (r'\.(?=[\w])', tok.Generic, 'attribute'),
            (r'[^\}]', tok.Generic),
            (r'\}', tok.Generic.Strong, '#pop'),
        ],
        'control': [
            (r'[\s]+\.', tok.Comment.Special),
            (r'[\s]*\$', tok.Generic.Strong, 'substitution'),
            (r'(comment|//)[^\n]*', tok.Comment.Special),
            (words(('select', 'one', 'any', 'many', 'from', 'for', 'each',
                    'end', 'instances', 'where', 'related', 'by', 'invoke',
                    'in', 'instance', 'break', 'while', 'assign', 'print',
                    'if', 'elif', 'else', 'create', 'object', 'exit', 'param',
                    'function', 'emit', 'to', 'file', 'clear', 'include',
                    'and', 'or', 'empty', 'not_empty', 'cardinality', 'not',
                    'first', 'not_first', 'last', 'not_last', 'selected'),
                   prefix=r'\b', suffix=r'\b'), tok.Keyword),
            (words(('boolean', 'integer', 'real', 'string', 'unique_id',
                    'inst_ref', 'inst_ref_set', 'frag_ref'),
                   prefix=r'\b', suffix=r'\b'), tok.Keyword.Type),
            (words(('get_env_var', 'put_env_var', 'shell_command',
                    'file_read', 'file_write', 'string_to_integer',
                    'string_to_real', 'integer_to_string', 'real_to_string',
                    'boolean_to_string'), prefix=r'\b', suffix=r'\b'), tok.Name.Builtin),
            (r'\d+[LlUu]*', tok.Number.Integer),
            (r'\b(true|false)\b', tok.Name.Constant),
            (r'[\s]+of[\s]+', tok.Keyword, 'class'),
            (r'(?i)R[0-9]+', tok.Number),
            (r'\.(?=[\w])', tok.Generic, 'attribute'),
            (r'(?i)[a-z_?][a-z_?0-9]*', tok.Name),
            (r'\->', tok.Operator, 'class'),
            (r'(\*|\+|-|\/|<|>|<=|>=|==|!=|=)', tok.Operator),
            (r'"', tok.String, 'string'),
            (r"'", tok.String, 'phrase'),
            (r'[^\n]', tok.Generic),
            (r'\n', tok.Generic, '#pop'),
        ],
        'class': [
            (r'[^\s\[]+', tok.Name.Class, '#pop'),
        ],
        'string': [
            (r'\$', tok.Generic.Strong, 'substitution'),
            (r'"', tok.String, '#pop'),
            (r'.', tok.String),
        ],
        'phrase': [
            (r"'", tok.String, '#pop'),
            (r'.', tok.String),
        ],
        'attribute': [
            (r'(?i)[a-z_?][a-z_?0-9]*', tok.Name, '#pop'),
        ],
    }

def setup(app):
    app.add_lexer("pyrsl", RSLLexer())


