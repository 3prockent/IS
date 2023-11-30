from teacher import Teacher
from group import Group

import time
import random
from numpy.random import rand
from numpy.random import randint
from collections import defaultdict

#constants
n_iter = 100
n_pop = 100
n_classes = 4
r_cross = 0.9
r_mut = 0.1

days = [
	"Monday", "Tuesday", "Wednesday", "Thursday", "Friday"
]

subjects = [
	'IS', 'SDMP', 'IT', 'DMT', 'MMS', 'English'
]

teachers = [
	Teacher(name="Tkachenko", subjects=["SDMP", "IT"], max_hours=15),
	Teacher(name="Voloshyn", subjects=["DMT"], max_hours=16),
	Teacher(name="Shyshatska", subjects=["IT"], max_hours=14),
	Teacher(name="Polyshcuk", subjects=["SDMP"], max_hours=16),
	Teacher(name="Trotsenko", subjects=["MMS"], max_hours=20),
	Teacher(name="Taranukha", subjects=["IS"], max_hours=15),
	Teacher(name="Fedorus", subjects=["IS"], max_hours=16),
	Teacher(name="Korobova", subjects=["DMT Science"], max_hours=10),
	Teacher(name="Krasovska", subjects=["English"], max_hours=12)
]

groups = [
    Group(group_name="TTP41", subjects_hours={"IT": 2, "IS": 1, "SDMP": 3, "English": 1, "MMS": 1}),
    Group(group_name="TTP42", subjects_hours={"IT": 2, "IS": 1, "SDMP": 3, "English": 1, "MMS": 1}),
	Group(group_name="TK41",  subjects_hours={"DMT": 2, "IS": 1, "SDMP": 1, "English": 1, "MMS": 3}),
    Group(group_name="MI41",  subjects_hours={"IT": 1, "IS": 3, "SDMP": 1, "English": 1, "MMS": 2}),
	Group(group_name="MI42",  subjects_hours={"IT": 1, "IS": 3, "SDMP": 1, "English": 1, "MMS": 2}),
]


def generate_population():
	population = list()
	for _ in range(n_pop):
		schedule = generate_schedule()
		population.append(schedule)
	return population


def generate_schedule():
	schedule = list()
	for group in groups:
		for subject, hours in group.subjects_hours.items():
			for _ in range(1, hours+1):
				cell = dict()
				cell["Day"] = random.choice(days)
				cell["Lesson"] = randint(1, n_classes+1)
				cell["Group"] = group
				cell["Subject"] = subject
				cell["Teacher"] = get_random_teacher(cell["Subject"])
				schedule.append(cell)
	return schedule


def get_random_teacher(subject):
    eligible_teachers = [teacher for teacher in teachers if subject in teacher.subjects]
    if eligible_teachers:
        return random.choice(eligible_teachers)
    else:
        return None


def crossover(p1, p2):
	c1, c2 = p1.copy(), p2.copy()
	pt = randint(1, len(p1)-2)
	c1 = p1[:pt] + p2[pt:]
	c2 = p2[:pt] + p1[pt:]
	return [c1, c2]


def selection(pop, scores):
	selection_ix = randint(len(pop))
	selection_iy = randint(len(pop))
	if scores[selection_ix] > scores[selection_iy]:
		return pop[selection_ix]
	else:
		return pop[selection_iy]


def mutation(schedule):
	for i in range(len(schedule)):
		if rand() < r_mut:
			schedule[i]["Day"] = random.choice(days)
			schedule[i]["Lesson"] = randint(1, n_classes+1)
	return schedule


def genetic_algorithm(objective, n_iter, n_pop):
	pop = generate_population()
	best, best_eval = pop[0], objective(pop[0])
	for gen in range(n_iter):
		print("Gen:", gen)
		scores = [objective(c) for c in pop]
		for i in range(n_pop):
			if scores[i] > best_eval:
				best, best_eval = pop[i], scores[i]
		print("Current best score:", best_eval)
		if best_eval >= 0.99:
			break
		new_population = []
		while len(new_population) < n_pop:
			p1 = selection(pop, scores)
			p2 = selection(pop, scores)
			child1, child2 = crossover(p1, p2)
			child1 = mutation(child1)
			child2 = mutation(child2)
			new_population.append(child1)
			new_population.append(child2)
		pop = new_population
	return [best, best_eval]


def accurate(schedule):
	def_teachers = defaultdict(dict)
	for i in range(len(schedule)):
		subject = schedule[i]["Subject"]
		teacher = schedule[i]["Teacher"]
		if teacher is not None:
			def_teachers[teacher][subject] = def_teachers[teacher].get(subject, 0) + 1
	teachers = dict(def_teachers)
	return ((teachers_accurate(teachers)) + calculate_fitness(schedule)) / 2


def teachers_accurate(teachers):
	score = 0
	for teacher, subjects_hours in teachers.items():
		total_hours = sum(subjects_hours.values())
		if total_hours <= teacher.max_hours:
			score += 1
	return score / len(teachers)


def calculate_fitness(schedule):
    conflicts = 0
    lessons_count = {}
    for lesson in schedule:
        key_g = (lesson["Day"], lesson["Lesson"], lesson["Group"])
        key_t = (lesson["Day"], lesson["Lesson"], lesson["Teacher"])
        lessons_count[key_g] = lessons_count.get(key_g, 0) + 1
    for count in lessons_count.values():
        if count >= 1:
            conflicts += count - 1
    return 1.0 / (conflicts + 1.0)


def main():
	best, score = genetic_algorithm(accurate, n_iter, n_pop)
	print("Done. Best: ", score)
	time.sleep(3)
	for b in best:
		print(b["Day"], b["Lesson"], b["Group"].group_name, b["Teacher"].name, b["Subject"])


if __name__ == '__main__':
	main()