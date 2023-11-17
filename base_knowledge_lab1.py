

questions = {
    'genre': 'What genre of book do you prefer?',
    'length': 'Do you prefer shorter, medium-length, or longer books?',
    'writing_style': 'Which writing style do you enjoy most in a book?',
    'plot_type': 'Do you prefer books with intricate plots or simpler storylines?'
}

book_conditions = {
    "Harry Potter Series": {
        "genre": "fantasy",
        "length": "longer",
        "writing_style": "descriptive",
        "plot_type": "intricate"
    },
    "Murder on the Orient Express": {
        "genre": "mystery",
        "length": "shorter",
        "writing_style": "intriguing",
        "plot_type": "simple"
    },
    "The Hitchhiker's Guide to the Galaxy": {
        "genre": "science_fiction",
        "length": "medium-length",
        "writing_style": "engaging",
        "plot_type": "simple"
    },
    "A Song of Ice and Fire Series": {
        "genre": "fantasy",
        "length": "longer",
        "writing_style": "intriguing",
        "plot_type": "intricate"
    },
    "The Girl with the Dragon Tattoo": {
        "genre": "mystery",
        "length": "medium-length",
        "writing_style": "descriptive",
        "plot_type": "simple"
    },
    "1984": {
        "genre": "science_fiction",
        "length": "shorter",
        "writing_style": "engaging",
        "plot_type": "simple"
    }
}

book_descriptions = {
    "Harry Potter Series": {
        "description": "A captivating series set in a world of magic, following the adventures of a young wizard and his friends."
    },
    "Murder on the Orient Express": {
        "description": "An intriguing murder mystery aboard a luxurious train, featuring the renowned detective Hercule Poirot."
    },
    "The Hitchhiker's Guide to the Galaxy": {
        "description": "A hilarious and mind-bending journey through space, filled with absurdity and wit."
    },
    "A Song of Ice and Fire Series": {
        "description": "An epic tale of political intrigue, power struggles, and mythical creatures set in a fantasy realm."
    },
    "The Girl with the Dragon Tattoo": {
        "description": "A gripping thriller delving into dark secrets and investigative journalism."
    },
    "1984": {
        "description": "A dystopian novel exploring surveillance, manipulation, and the struggle for individuality in a totalitarian society."
    }
}


def genre():
    answer = None
    while answer not in ['fantasy', 'mystery', 'science_fiction']:
        answer = input(f"{questions['genre']} (fantasy/mystery/science_fiction) ")
    return answer

def length():
    answer = None
    while answer not in ['shorter', 'medium-length', 'longer']:
        answer = input(f"{questions['length']} (shorter/medium-length/longer) ")
    return answer

def writing_style():
    answer = None
    while answer not in ['descriptive', 'intriguing', 'engaging']:
        answer = input(f"{questions['writing_style']} (descriptive/intriguing/engaging) ")
    return answer

def plot_type():
    answer = None
    while answer not in ['intricate', 'simple']:
        answer = input(f"{questions['plot_type']} (intricate/simple) ")
    return answer

def find_book():
    selected_conditions = {
        'genre': genre(),
        'length': length(),
        'writing_style': writing_style(),
        'plot_type': plot_type()
    }

    matching_books = []

    for book, conditions in book_conditions.items():
        if all(conditions[key] == selected_conditions[key] for key in conditions):
            matching_books.append(book)

    if matching_books:
        print("Based on your preferences, the following books may suit you:")
        for book in matching_books:
            print(book_descriptions[book]['description'])
    else:
        print("Sorry, we couldn't find a matching book based on your preferences.")


def main():
    print('What type of book suits you best?')
    find_book()


if __name__ == "__main__":
    main()
