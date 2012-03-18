# -*- coding: UTF-8 -*-

import ply.lex as lex

import os



literals = "{};:,=()[].<>?"



tokens = [
  "INTEGER",
  "FLOAT",
  "IDENTIFIER",
  "STRING",
  "WHITESPACE",
  "OTHER",
  "ELLIPSIS",
]



keywords = (
  "Date",
  "DOMString",
  "any",
  "attribute",
  "boolean",
  "byte",
  "callback",
  "const",
  "creator",
  "deleter",
  "dictionary",
  "double",
  "enum",
  "exception",
  "false",
  "float",
  "getter",
  "implements",
  "inherit",
  "interface",
  "legacycaller",
  "long",
  "null",
  "object",
  "octet",
  "optional",
  "or",
  "partial",
  "readonly",
  "sequence",
  "setter",
  "short",
  "static",
  "stringifier",
  "true",
  "typedef",
  "unsigned",
  "void",
)



tokens.extend(keywords)



t_ignore = ' \t'
t_ignore_line_comment = r'//.*'


t_INTEGER = r"-?(0([0-7]*|[Xx][0-9A-Fa-f]+)|[1-9][0-9]*)"
t_STRING = r"\"[^\"]*\""
t_WHITESPACE = r"[\t\n\r ]+|[\t\n\r ]*((//.*|/\*.*?\*/)[\t\n\r ]*)+"
t_ELLIPSIS = r"\.\.\."



def t_IDENTIFIER(t):
  r"[A-Z_a-z][0-9A-Z_a-z]*"
  if t.value in keywords:
    t.type = t.value
  return t



def t_block_comment(t):
  r"\/\*[^*]*\*+([^/*][^*]*\*+)*\/"
  t.lexer.lineno += t.value.count('\n')



def t_newline(t):
  r"\n"
  t.lexer.lineno += 1



def t_error(t):
  print "Illegal character '%s' at %d" % (t.value[0], t.lexer.lineno)
  t.lexer.skip(1)



lexdir = os.path.dirname(__file__)
lex.lex(lextab="pywidl.lextab", outputdir=lexdir, optimize=0)