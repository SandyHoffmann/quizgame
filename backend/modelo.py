from config import *

class Quiz(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    assuntoquiz = db.Column(db.String(254))

    def __str__(self):
        return self.id+ str(self.assuntoquiz)
    
    def json(self):
        return {
            "id": self.id,
            "assuntoquiz": self.assuntoquiz
        }

class Resultado(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    resultado = db.Column(db.String(254))
    quizidr = db.Column(db.Integer,db.ForeignKey(Quiz.id),nullable=False)
    quizr = db.relationship("Quiz")

    def __str__(self):
        return self.id+ str(self.resultado)+", "+self.quizidr+", "+str(self.quizr)
    
    def json(self):
        return {
            "id": self.id,
            "resultado": self.resultado,
            "quizidr": self.quizidr,
            "quizr":self.quizr.json()
        }

class Pergunta(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    pergunta = db.Column(db.String(254))
    quizidp = db.Column(db.Integer,db.ForeignKey(Quiz.id),nullable=False)
    quizp = db.relationship("Quiz")

    def __str__(self):
        return self.id+ str(self.pergunta)+", "+self.quizidp+", "+str(self.quizp)
    
    def json(self):
        return {
            "id": self.id,
            "pergunta": self.pergunta,
            "quizidr": self.quizidp,
            "quizr":self.quizp.json()
        }


class Alternativa(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    alternativas = db.Column(db.String(254))
    perguntaid = db.Column(db.Integer,db.ForeignKey(Pergunta.id),nullable=False)
    perguntaa = db.relationship("Pergunta")

    def __str__(self):
        return self.id+ str(self.alternativas)+", "+self.perguntaid+", "+str(self.perguntaa)
    
    def json(self):
        return {
            "id": self.id,
            "alternativas": self.alternativas,
            "perguntaid": self.perguntaid,
            "perguntaa":self.perguntaa.json()
        }