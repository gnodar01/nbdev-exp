# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.17.0
#   kernelspec:
#     display_name: Python 3 (ipyflow)
#     language: python
#     name: ipyflow
# ---

# %% [markdown]
# # core
#
# > Fill in a module description here

# %%
#| default_exp core

# %%
#| hide
from nbdev.showdoc import *


# %%
#| export
def foo(): return 'foo'

# %%
#| export
def bar(): return 'bar'


# %%
#| export
def baz(): return 'baz'


# %%
#| hide
import nbdev; nbdev.nbdev_export()

# %%
#| hide
x = 0


# %%
#| hide
def get_x():
    return x


# %%
#| hide
y = 2

# %%
get_x() + y

# %%
