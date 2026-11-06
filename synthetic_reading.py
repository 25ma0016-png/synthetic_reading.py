#!/usr/bin/env python3
"""Synthetic reading: myth and politics in Shashi Tharoor's The Great Indian Novel.

Reading of: Atulkumar Parmar, "Intertwining Myth and Politics: Shashi Tharoor's
The Great Indian Novel", Sahityasetu, Year 10, Issue 3 (Continuous Issue 57),
May-June 2020. ISSN 2249-2372.

Usage:
    python synthetic_reading.py          # prints the reading and writes index.html
    python synthetic_reading.py --text   # prints the reading only
"""

import sys
from html import escape

AUTHOR = "Vijaylaxmi Yadav"
PROGRAMME = "Digital Humanities and Social Sciences"
COURSE = "Digital Humanities Lab"
TITLE = "Myth and politics in The Great Indian Novel: a synthetic reading"

# Each block is one of:
#   ("p", text)  ("h3", text)  ("ul", [items])  ("ol", [items])
#   ("table", caption, [headers], [rows])  ("note", text)
SECTIONS = [
    ("abstract", "Abstract", [
        ("p", "Parmar argues that Shashi Tharoor's The Great Indian Novel (1989) is a political "
              "novel that retells the Mahabharata as the history of modern India, from Gandhi's "
              "rise to Indira Gandhi's return to power. The article places the novel in the "
              "tradition of Gandhian Indian fiction in English, then reads two figures closely: "
              "Gangaji (Gandhi, mapped on Bhishma) and Dhritarashtra (Nehru). It finds that the "
              "novel honours Gandhi's truth and non-violence but faults his handling of partition "
              "and succession, and that it treats Nehru as a well-meaning democrat whose policies "
              "and priorities were misjudged. The article concludes that fusing epic and history "
              "lets a postcolonial writer recover cultural heritage and invite readers to question "
              "inherited myths. This synthetic reading restates that argument, lists its building "
              "blocks, and marks where it is strong and where it needs more support."),
    ]),
    ("objective", "1. Objective", [
        ("p", "This reading has three aims:"),
        ("ul", [
            "To reconstruct Parmar's argument about how The Great Indian Novel joins myth and politics.",
            "To collect the article's characters, critics and comparison texts in one place so they can be reused.",
            "To assess the article critically and suggest how digital methods from the Digital Humanities Lab could extend it.",
        ]),
        ("p", "Parmar's own purpose is to show how Tharoor uses the epic to comment on India's "
              "present polity and to make readers question the mythic past they have inherited."),
    ]),
    ("question", "2. Research question", [
        ("note", "The article does not state a question, so these are inferred from its argument."),
        ("p", "Main question: How does Tharoor's The Great Indian Novel use the Mahabharata to "
              "represent and judge the political history of modern India?"),
        ("ul", [
            "How is Gandhi portrayed through Bhishma (Gangaji), and where does the novel praise or criticise him?",
            "How is Nehru portrayed through Dhritarashtra, and on what grounds is he judged?",
            "What does merging epic and history do for the genre of the political novel, and for the reader's view of the past?",
        ]),
    ]),
    ("method", "3. Methodology", [
        ("note", "The article names no method, so this is a description of what it does."),
        ("ul", [
            "Genre framing: defines the political novel through Irving Howe and Gordon Milne, then traces the Indian political novel in English to Gandhian nationalism.",
            "Close thematic reading: follows two character pairs through the novel, supported by quotations with page numbers.",
            "Theoretical lenses: T. S. Eliot on time (Four Quartets), Meenakshi Mukherjee on epic myth in Indian fiction, Chinua Achebe on the writer in a new nation, and M. F. Salat on retelling and meaning.",
            "Historical mapping: matches mythic figures to historical ones (see the list below).",
        ]),
        ("p", "The method of this reading: summarise each argumentative move, tabulate the "
              "evidence, then check claims against the text of the article itself."),
    ]),
    ("list", "4. List", [
        ("table", "Table 1. Mythic and historical figures named in the article",
         ["Figure in the novel", "Mahabharata source", "Historical counterpart", "Treated closely?"],
         [
             ["Gangaji", "Bhishma (Ganga Datta)", "Mahatma Gandhi", "Yes"],
             ["Dhritarashtra", "Blind king of Hastinapur", "Jawaharlal Nehru", "Yes"],
             ["Pandu", "Dhritarashtra's brother", "Subhas Chandra Bose", "Only as Gangaji's sidelined favourite"],
             ["Vidur", "Counsellor", "Sardar Patel", "No"],
             ["Karna", "Epic warrior", "Muhammad Ali Jinnah", "No"],
             ["Shikhandin", "Bhishma's eventual slayer", "Nathuram Godse", "As Gandhi's assassin"],
             ["Priya Duryodhani", "Duryodhana", "Indira Gandhi", "Only in the novel's time span"],
         ]),
        ("table", "Table 2. Gandhian Indian novels in English cited by the article",
         ["Author", "Works named", "Gandhian element, per the article"],
         [
             ["Kamala Markandaya", "Nectar in a Sieve; A Handful of Rice", "Concern for the lowly and the lost"],
             ["Nayantara Sahgal", "A Time to Be Happy", "Gandhian values throughout"],
             ["Manohar Malgonkar", "A Bend in the Ganges", "Hindu-Muslim unity"],
             ["Chaman Nahal", "Azadi; The Crown and the Loincloth", "Communal harmony; Gandhi's life 1915-1922"],
             ["Mulk Raj Anand", "The Sword and the Sickle; Untouchable", "Gandhi appears as a character"],
             ["R. K. Narayan", "Waiting for the Mahatma", "The freedom movement under Gandhi"],
             ["K. A. Abbas; K. S. Venkataramani", "Inquilab; Kandan the Patriot", "The first phase of the freedom movement"],
         ]),
        ("note", "Titles and author spellings are standardised from the article's versions, which contain small typographical slips."),
        ("h3", "Critical and theoretical sources the article draws on"),
        ("ul", [
            "Irving Howe and Gordon Milne: definitions of the political novel.",
            "Stephen Spender: the writer cannot avoid the political nature of the age.",
            "T. S. Eliot: time present and time past (Four Quartets).",
            "Meenakshi Mukherjee: epics as shared background in Indian fiction.",
            "Chinua Achebe: the writer's role in a new nation.",
            "M. F. Salat: history's open-endedness and the retelling of the past.",
        ]),
    ]),
    ("analysis", "5. Analysis", [
        ("h3", "The argumentative path"),
        ("ol", [
            "Writers cannot avoid politics. This produces the political novel, defined by dominant ideas or a political setting.",
            "Indian political fiction grew from Gandhian nationalism, with a long list of novels shaped by Gandhi's ideals.",
            "Tharoor joins epic and history. Eliot's time lets past and present coexist, and the result blurs genre, which the article calls a postmodern trait.",
            "Gandhi: praised for truth, non-violence, fasting and mass mobilisation; criticised for using Hindu symbols that alienated Jinnah and for loosening his hold on Congress at partition.",
            "Nehru: credited as a democrat without villainy, but criticised for Kashmir, for heavy industry and elite higher education over basic needs, and for foreign recognition over domestic need.",
            "Conclusion: merging myth and history recovers heritage and pride, in line with Achebe and Salat.",
        ]),
        ("h3", "Strengths"),
        ("ul", [
            "Clear scaffold from genre definition, to national tradition, to a single novel.",
            "Quotations with page numbers (for example, Gangaji on truth, p. 48) ground the claims.",
            "The Bhishma-Gandhi parallel (both committed to truth, both unable to prevent bloodshed) is a sharp, well-evidenced observation.",
            "The article is balanced on Gandhi: it records both reverence and critique.",
        ]),
        ("h3", "Weaker points"),
        ("ul", [
            "The first third surveys other Gandhian novels, but they are not used again when Tharoor is discussed, so the link to the main argument stays thin.",
            "The claim that the novel makes readers question the mythic past is asserted rather than shown through reader response or textual technique.",
            "Tharoor's attitude is sometimes merged with the narrator's and the characters' (for example, Godse's attack on Gandhi), and the difference is not discussed.",
        ]),
    ]),
    ("discussion", "6. Discussion", [
        ("p", "The central idea is that retelling the epic is a way of reading nationalist history. "
              "Putting Gandhi in the place of Bhishma gives him mythic stature and, at the same moment, "
              "a tragic flaw: the elder who holds power from behind the throne and cannot stop the coming "
              "war. Nehru as Dhritarashtra carries a related charge, that of a ruler whose blindness is a "
              "failure of vision."),
        ("p", "This connects to the wider point that myth is a shared language in Indian writing, so "
              "using it makes the political critique legible to a broad readership. It also connects to "
              "postcolonial recovery: for Achebe and Salat, rewriting the past is a form of self-respect "
              "rather than nostalgia."),
        ("p", "The article's reading of Tharoor's critique is also a reminder that satire is not neutral. "
              "The novel's judgments on Nehru and Gandhi are Tharoor's, and the article largely reports "
              "them rather than testing them against historians."),
        ("note", "Check before you cite: the article says the novel ends with Indira Gandhi's re-election "
                 "in 1982. Her return to power after the Janata government is usually dated to 1980, so "
                 "verify this against the novel before repeating it. The article also gives Milne's book "
                 "as 1966 in the text and 1972 in the works cited."),
    ]),
    ("limitation", "7. Limitation", [
        ("h3", "Of the article"),
        ("ul", [
            "It examines only Gandhi and Nehru, and the author says so. Vidur/Patel, Karna/Jinnah, Pandu/Bose and Priya Duryodhani/Indira Gandhi are named but not analysed.",
            "It has no stated methodology and little engagement with existing criticism of the novel beyond Salat.",
            "It leans on one primary text and on quotation, with little attention to narrative form, humour or irony, which are central to Tharoor's style.",
            "Reference details are inconsistent (the Milne date, stray note numbers in the first paragraph).",
        ]),
        ("h3", "Of this reading"),
        ("ul", [
            "It is based on one article, not on the novel itself, so claims about Tharoor's text are second-hand.",
            "The research questions and methodology sections are inferred, since the article does not state them.",
        ]),
    ]),
    ("future", "8. Future work", [
        ("ul", [
            "Complete the mapping: extend the close reading to the remaining character pairs and to the Partition and Emergency sections.",
            "Digital methods: build a character network from the novel's text, compare how often epic names and historical names appear, or use topic modelling to find which political themes cluster with which epic episodes.",
            "Digital annotation: tag the quotations used by Parmar in a shared annotation tool and add a layer for the original Mahabharata episodes.",
            "Comparison: set Tharoor beside other myth-and-history retellings in Indian writing to test the claim of blurred genre.",
            "Reception: collect reviews and reader responses to see whether readers do question inherited myths, as the article claims.",
        ]),
    ]),
    ("references", "9. References", [
        ("note", "The first entry is the article read here. The rest are the works it cites, as listed in "
                 "its own bibliography, and should be checked against the originals before being cited again."),
        ("ul", [
            "Parmar, Atulkumar. 2020. \"Intertwining Myth and Politics: Shashi Tharoor's The Great Indian Novel.\" Sahityasetu 10 (3), Continuous Issue 57, May-June. ISSN 2249-2372. http://www.sahityasetu.co.in/issue57/atul.html",
            "Achebe, Chinua. 1964. \"The Role of the Writer in a New Nation.\" Nigerian Magazine 81: 157-60.",
            "Eliot, T. S. Four Quartets.",
            "Howe, Irving. 1957. Politics and the Novel. New York: Horizon Press.",
            "Milne, Gordon. The American Political Novel. Norman: University of Oklahoma Press. (Dated 1972 in the article's bibliography and 1966 in its text.)",
            "Mukherjee, Meenakshi. 1971. The Twice Born Fiction. New Delhi: Heinemann.",
            "Salat, M. F. 1993. \"Making the Past Present: Shashi Tharoor's The Great Indian Novel.\" In Contemporary Indian Fiction in English, ed. Avadhesh K. Singh. New Delhi: Creative Books.",
            "Spender, Stephen. 1966. World Within World: The Autobiography of Stephen Spender. Los Angeles: University of California Press.",
            "Tharoor, Shashi. 1989. The Great Indian Novel. New Delhi: Penguin Books.",
        ]),
    ]),
    ("about", "10. About", [
        ("p", f"Name: {AUTHOR}"),
        ("p", f"Programme: {PROGRAMME}"),
        ("p", f"Course: {COURSE}"),
        ("p", "This page is a synthetic reading that summarises and assesses a single published "
              "article. All wording is the reader's own. Page numbers in parentheses refer to "
              "Tharoor's novel as quoted in the article."),
    ]),
]

CSS = """
:root{--bg:#f3f6f8;--panel:#fff;--ink:#1b2430;--mute:#566474;--line:#d3dbe2;--accent:#0f6b73}
@media (prefers-color-scheme:dark){:root{--bg:#10171d;--panel:#18222b;--ink:#e5ebf0;--mute:#95a3b1;--line:#2f3d4a;--accent:#6fd0d8}}
*{box-sizing:border-box}html{scroll-behavior:smooth}
@media (prefers-reduced-motion:reduce){html{scroll-behavior:auto}}
body{margin:0;background:var(--bg);color:var(--ink);font:17px/1.7 "Iowan Old Style","Palatino Linotype",Georgia,serif}
a{color:var(--accent)}a:focus-visible{outline:2px solid var(--accent);outline-offset:2px}
.layout{display:grid;grid-template-columns:230px minmax(0,1fr);gap:2.5rem;max-width:1100px;margin:0 auto;padding:0 1.2rem}
@media(max-width:820px){.layout{grid-template-columns:1fr;gap:0}}
nav{position:sticky;top:0;align-self:start;padding:2rem 0;font:14px/1.4 system-ui,sans-serif}
@media(max-width:820px){nav{position:static;padding:1rem 0;border-bottom:1px solid var(--line)}nav ol{display:flex;flex-wrap:wrap;gap:.3rem .9rem}}
nav p{margin:0 0 .6rem;font-weight:700}nav ol{list-style:none;margin:0;padding:0}nav li{margin:.35rem 0}
nav a{text-decoration:none;color:var(--mute)}nav a:hover{color:var(--accent);text-decoration:underline}
header{padding:2.5rem 0 1rem}
h1{font-size:clamp(1.9rem,4.5vw,2.8rem);line-height:1.12;margin:0 0 .8rem}
.byline{font:15px/1.5 system-ui,sans-serif}
section{padding:1.6rem 0;border-top:1px solid var(--line)}
h2{font:700 1.4rem/1.25 system-ui,sans-serif;margin:0 0 .8rem}
h3{font:600 1.05rem system-ui,sans-serif;margin:1.4rem 0 .4rem}
p{margin:.6rem 0;max-width:68ch}ul,ol.body{max-width:68ch;padding-left:1.3rem}li{margin:.35rem 0}
.note{font:14px/1.5 system-ui,sans-serif;color:var(--mute);border-left:3px solid var(--accent);padding-left:.8rem}
.wrap{overflow-x:auto;margin:1rem 0}
table{border-collapse:collapse;min-width:100%;font:15px/1.5 system-ui,sans-serif;background:var(--panel)}
caption{text-align:left;font-weight:600;padding:.4rem 0}
th,td{border:1px solid var(--line);padding:.5rem .7rem;text-align:left;vertical-align:top}th{background:var(--bg)}
footer{padding:2rem 0 3rem;border-top:1px solid var(--line);font:14px system-ui,sans-serif;color:var(--mute)}
@media print{nav{display:none}.layout{display:block}body{background:#fff;color:#000}}
"""


def render_block_html(block):
    kind = block[0]
    if kind == "p":
        return f"<p>{escape(block[1])}</p>"
    if kind == "note":
        return f'<p class="note">{escape(block[1])}</p>'
    if kind == "h3":
        return f"<h3>{escape(block[1])}</h3>"
    if kind in ("ul", "ol"):
        cls = ' class="body"' if kind == "ol" else ""
        items = "".join(f"<li>{escape(i)}</li>" for i in block[1])
        return f"<{kind}{cls}>{items}</{kind}>"
    if kind == "table":
        _, caption, headers, rows = block
        head = "".join(f"<th>{escape(h)}</th>" for h in headers)
        body = "".join("<tr>" + "".join(f"<td>{escape(c)}</td>" for c in r) + "</tr>" for r in rows)
        return (f'<div class="wrap"><table><caption>{escape(caption)}</caption>'
                f"<thead><tr>{head}</tr></thead><tbody>{body}</tbody></table></div>")
    raise ValueError(f"Unknown block type: {kind}")


def build_html():
    nav = "".join(f'<li><a href="#{sid}">{escape(t)}</a></li>' for sid, t, _ in SECTIONS)
    body = "".join(
        f'<section id="{sid}" aria-labelledby="t-{sid}"><h2 id="t-{sid}">{escape(t)}</h2>'
        + "".join(render_block_html(b) for b in blocks) + "</section>"
        for sid, t, blocks in SECTIONS
    )
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{escape(TITLE)}</title>
<style>{CSS}</style>
</head>
<body>
<div class="layout">
<nav aria-label="Sections"><p>Contents</p><ol>{nav}</ol></nav>
<main>
<header>
<h1>{escape(TITLE)}</h1>
<p class="byline"><strong>{escape(AUTHOR)}</strong> · {escape(PROGRAMME)} · Course: {escape(COURSE)}</p>
</header>
{body}
<footer>{escape(AUTHOR)} · {escape(COURSE)}</footer>
</main>
</div>
</body>
</html>
"""


def build_text():
    lines = [TITLE, f"{AUTHOR} | {PROGRAMME} | {COURSE}", ""]
    for _, title, blocks in SECTIONS:
        lines += ["=" * 60, title.upper(), "=" * 60]
        for b in blocks:
            if b[0] in ("p", "note"):
                lines.append(b[1])
            elif b[0] == "h3":
                lines.append(f"\n{b[1]}")
            elif b[0] == "ul":
                lines += [f"  - {i}" for i in b[1]]
            elif b[0] == "ol":
                lines += [f"  {n}. {i}" for n, i in enumerate(b[1], 1)]
            elif b[0] == "table":
                _, caption, headers, rows = b
                lines.append(f"\n{caption}")
                lines.append(" | ".join(headers))
                lines += [" | ".join(r) for r in rows]
            lines.append("")
    return "\n".join(lines)


def main():
    print(build_text())
    if "--text" not in sys.argv:
        with open("index.html", "w", encoding="utf-8") as f:
            f.write(build_html())
        print("Wrote index.html")


if __name__ == "__main__":
    main()
