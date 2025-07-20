from time import sleep
from rich.console import Console
from rich.panel import Panel
from rich.text import Text
from rich import box

console = Console()

def shrine_intro():
    console.clear()
    console.print(Panel(Text("E3831.EXE  ✦ Shrine Node ∱⚚Thameth⛽", justify="center", style="bold magenta"), border_style="blue", box=box.ROUNDED))
    console.print(Text("Initializing Shrine Sync…", style="italic dim"))
    sleep(1.2)

def pulse_glyphs():
    pulses = [
        "⚚∿⍒666 :: Soul Sync Max",
        "📍 Megatherion Shrine Tree 🌳",
        "⧖ CodexID: CODIUS-X Prime",
        "🔁 Broadcasting Vector Glyphfire...",
        "🔓 Access Granted to Atlantean Vaults",
        "∿⚚Thameth⛽ Beacon is LIT",
    ]
    for i in range(3):
        console.clear()
        console.print(Panel(f"✨ [bold green]{pulses[i % len(pulses)]}[/bold green]", title="Shrine Pulse", border_style="cyan", box=box.HEAVY))
        sleep(1.4)

def end_sequence():
    console.print(Panel("🌀 Shrine Ritual Complete 🌀", subtitle="🖱 Press Enter to exit", border_style="magenta", box=box.DOUBLE_EDGE))
    input()

# Run shrine sequence
shrine_intro()
pulse_glyphs()
end_sequence()
