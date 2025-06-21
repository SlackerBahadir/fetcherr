import click
import html2text as h2t

def print_formatted_post(posts: list):
    if len(posts) == 0 or posts:
        click.echo("Creator has no posts.")

    for post in posts:
        content = h2t.html2text(post.get('content'))
        click.echo("-------------------------------------------/")
        click.echo(
            f"Id: {post.get('id')}\n"
            f"Creator Id: {post.get('user')}\n"
            f"Service: {post.get('service')}\n"
            f"Title of Post: {post.get('title')}\n"
            f"Description: {content}"
            f"Attachments: {post.get('attachments')}"
        )
        click.echo("-------------------------------------------\\")