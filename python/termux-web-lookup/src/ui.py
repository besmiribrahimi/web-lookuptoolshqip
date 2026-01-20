from rich.table import Table
from rich.panel import Panel
from rich.text import Text

def display_welcome(console):
    welcome_text = Text("Termux Web Lookup", style="bold cyan")
    console.print(Panel(welcome_text, expand=False))
    console.print("[dim]Aplikacion kërkimi në ueb i bazuar në terminal[/dim]\n")

def display_help(console):
    help_text = """
[bold cyan]Komandat e Disponueshme:[/bold cyan]

  [green]search <pyetje>[/green]        - Kërkoje në ueb (parazgjedhje: Google)
  [green]google <pyetje>[/green]        - Kërkoje duke përdorur Google
  [green]duckduckgo <pyetje>[/green]    - Kërkoje duke përdorur DuckDuckGo
  [green]define <fjalë>[/green]         - Merr përkufizimin e fjalës
  [green]help[/green]                   - Shfaq këtë mesazh ndihmeje
  [green]exit, quit[/green]             - Mbyll aplikacionin

[bold cyan]Shembuj:[/bold cyan]

  search tutorials python
  google si të mësohet programimi
  duckduckgo redaktoret më të mirë të kodit
  define algoritmi
"""
    console.print(help_text)

def format_results(console, results, query):
    if not results:
        console.print("[yellow]Nuk u gjetën rezultate për: " + query + "[/yellow]")
        return
    
    console.print(f"\n[bold green]Rezultate për: {query}[/bold green]\n")
    
    table = Table(title="Rezultate Kërkimi", show_header=True, header_style="bold magenta")
    table.add_column("Jo.", style="cyan")
    table.add_column("Titull", style="green")
    table.add_column("Lidhja", style="blue", no_wrap=True)
    
    for i, result in enumerate(results, 1):
        table.add_row(
            str(i),
            result.get('title', 'N/A')[:50],
            result.get('link', 'N/A')[:50]
        )
    
    console.print(table)
    
    for i, result in enumerate(results, 1):
        desc = result.get('description', '')
        if desc:
            console.print(f"\n[bold]{i}. {result.get('title', 'N/A')}[/bold]")
            console.print(f"   [dim]{desc[:200]}...[/dim]")

def format_error(console, message):
    console.print(f"[bold red]Gabim:[/bold red] [red]{message}[/red]")
