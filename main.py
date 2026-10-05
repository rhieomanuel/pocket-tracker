from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.prompt import Prompt, IntPrompt
from storage import load_data, save_data
from tracker import calculate_summary

console = Console()

def show_dashboard():
    data = load_data()
    summary = calculate_summary(data)

    console.clear()
    console.print(Panel.fit("[bold cyan]POCKET TRACKER - PENGHITUNG HARTA[/bold cyan]", border_style="cyan"))

    table = Table(title="Ringkasan Harta")
    table.add_column("Keterangan cugs", style="bold")
    table.add_column("Jumlah (Rp)", justify="right")

    table.add_row("Total Pemasukan", f"Rp {summary['total_income']:,}")
    table.add_row("Total Pengeluaran", f"Rp {summary['total_expense']:,}")
    table.add_row("Sisa Harta", f"Rp {summary['net_balance']:,}", style="bold green" if summary['net_balance'] >= 0 else "bold red")
    console.print(table)

    console.print(f"\n[bold]Tingkat Keborosan:[/bold] [{summary['color']}]{summary['burn_rate']:.1f}% ({summary['status']})[/{summary['color']}]")
    console.print(f"[bold]Perbandingan Cashflow:[/bold] Masuk {summary['income_pct']:.1f}% | Keluar {summary['expense_pct']:.1f}%")

    if summary['category_percentages']:
        cat_table = Table(title="Persentase Pengeluaran per Kategori")
        cat_table.add_column("Kategori")
        cat_table.add_column("Persentase", justify="right")
        for cat, pct in summary['category_percentages'].items():
            cat_table.add_row(cat, f"{pct:.1f}%")
        console.print(cat_table)

def add_transaction():
    data = load_data()
    t_type = Prompt.ask("Jenis Transaksi", choices=["income", "expense"])
    desc = Prompt.ask("Keterangan/Catatan")
    amount = IntPrompt.ask("Nominal (Rp)")

    category = "Pemasukan"
    if t_type == "expense":
        category = Prompt.ask("Kategori", choices=["Jajan", "Transport", "Print/Tugas", "Lainnya"])

    data["transactions"].append({
        "type": t_type,
        "description": desc,
        "amount": amount,
        "category": category
    })

    save_data(data)
    console.print("[bold green]Transaksi berhasil dicatat![/bold green]")

def main():
    while True:
        console.print("\n[bold yellow]MENU UTAMA:[/bold yellow]")
        console.print("1. Lihat Dashboard & Analisis Keborosan")
        console.print("2. Tambah Transaksi")
        console.print("3. Keluar")

        choice = Prompt.ask("Pilih menu", choices=["1", "2", "3"])
        if choice == "1":
            show_dashboard()
        elif choice == "2":
            add_transaction()
        elif choice == "3":
            console.print("[bold cyan]Sampai jumpa![/bold cyan]")
            break

if __name__ == "__main__":
    print("Aplikasi berjalan...")
    main()