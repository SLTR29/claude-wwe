"""WWE Tracker - Track wrestlers, events, and match results."""


def get_wrestlers():
    return [
        {"name": "Roman Reigns", "brand": "SmackDown", "title": "Undisputed WWE Champion"},
        {"name": "Cody Rhodes", "brand": "Raw", "title": "WWE Champion"},
        {"name": "Rhea Ripley", "brand": "Raw", "title": "Women's World Champion"},
        {"name": "Bianca Belair", "brand": "SmackDown", "title": None},
    ]


def display_roster(wrestlers):
    print("=== WWE Roster ===\n")
    for w in wrestlers:
        title = w["title"] if w["title"] else "No current title"
        print(f"  {w['name']} ({w['brand']}) - {title}")
    print()


def main():
    wrestlers = get_wrestlers()
    display_roster(wrestlers)
    print(f"Total wrestlers tracked: {len(wrestlers)}")


if __name__ == "__main__":
    main()
