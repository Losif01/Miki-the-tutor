# main.py - Miki, Your Personal Study Buddy (Markdown-enabled)
import sys
from pathlib import Path
from rich.console import Console
from rich.markdown import Markdown
from rich.panel import Panel
from rich.text import Text
from rich.markup import escape as escape_markup

# Add project root to path so imports work
sys.path.append(str(Path(__file__).parent))

from rag.qa_chain import get_qa_chain


def main():
    console = Console()
    console.print(Panel("📘 Miki - Your Personal Study Buddy", style="bold magenta", expand=False))
    console.print("Loading QA system... (this may take a few seconds)\n", style="italic")

    try:
        qa = get_qa_chain()
    except Exception as e:
        # Escape exception message
        console.print(f"[red]❌ Failed to load QA system: {escape_markup(str(e))}[/red]")
        console.print("\n💡 Make sure you've built the index with:")
        # Use valid style instead of [code] → use 'repr.code' or 'cyan on black'
        console.print(
            Text("python -c 'from ingestion.build_index import build_vector_index; build_vector_index()'",
                 style="cyan on black")
        )
        return

    console.print("[green] Miki is ready![/green] Type your questions below.")
    console.print("[dim] Type 'quit', 'exit', or Ctrl+C to exit.\n[/dim]")

    while True:
        try:
            question = console.input("[bold cyan]❓ Question:[/bold cyan] ").strip()
            if not question:
                console.print("[yellow]Please ask a question.[/yellow]\n")
                continue
            if question.lower() in {"quit", "exit", "bye"}:
                console.print("[bold green]👋 Goodbye! Happy studying![/bold green]")
                break

            console.print("[bold blue] Thinking...[/bold blue]\n")

            result = qa.invoke({"query": question})

            # Render answer as Markdown (safe)
            console.print("[bold] Answer -> [/bold]")
            safe_answer = escape_markup(result["result"].strip())
            console.print(Markdown(safe_answer))
            console.print("")

            # Show sources
            if result.get("source_documents"):
                console.print("[bold] Source:[/bold]")
                for i, doc in enumerate(result["source_documents"], 1):
                    src = doc.metadata.get("source", "unknown")
                    page = doc.metadata.get("page", "N/A")
                    console.print(f"   {i}. [italic]{src}[/italic], page {page}")
            else:
                console.print("[yellow]⚠️ No sources retrieved (might be out of context).[/yellow]")

            console.print("[dim]" + "-" * 50 + "[/dim]\n")

        except KeyboardInterrupt:
            console.print("\n[bold green] Goodbye! Happy studying![/bold green]")
            break
        except Exception as e:
            # Always escape exception messages
            console.print(f"[red]⚠️ Error getting answer: {escape_markup(str(e))}[/red]")
            console.print("[dim]Try another question or restart.[/dim]\n")


if __name__ == "__main__":
    main()