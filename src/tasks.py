from invoke import task
from tetris import Game

@task
def foo(ctx):
    print("bar")

@task
def start(ctx):
    ctx.run("python3 tetris.py")

@task
def test(ctx):
    ctx.run("pytest")

@task
def coverage(ctx):
    ctx.run("coverage run --branch -m pytest")

@task()
def coverage_report(ctx):
    ctx.run("coverage html")
