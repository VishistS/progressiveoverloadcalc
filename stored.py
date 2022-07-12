class Data:
    def __init__(self, exerc, wgt, set, rep):
        self.exercisechosen = exerc
        self.weight = wgt
        self.sets = set
        self.reps = rep

    def checkdata(self):
        try:
            int(self.weight)
            int(self.sets)
            int(self.reps)
        except:
            return False

    def overload(self):
        convertedreps = int(self.reps)
        convertedweight = int(self.weight)
        if self.exercisechosen == 'Dumbbell':
            if convertedreps >= 12:
                self.weight = convertedweight + 2.5
                self.reps = 6
                return self.weight, self.reps
            if convertedreps < 12:
                self.reps = convertedreps + 2
                return self.weight, self.reps
        if self.exercisechosen == 'Barbell':
            if convertedreps >= 12:
                self.weight = convertedweight + 5
                self.reps = 6
                return self.weight, self.reps
            if convertedreps < 12:
                self.reps = convertedreps + 4
                return self.weight, self.reps
        if self.exercisechosen == 'Calisthenics':
            return False
