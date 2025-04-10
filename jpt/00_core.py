# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.17.0
#   kernelspec:
#     display_name: ipyflow
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
from fastcore.test import*


# %%
#| export
def foo(): pass


# %%
#| export
def bar(): return "bar"


# %%
#| hide
assert bar() == "bar"


# %%
#| export
def baz(): return "baz"


# %%
#| hide
test_eq(baz(), "baz")

# %%
#| hide
import nbdev; nbdev.nbdev_export()

# %%
#| hide
x = 8


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
