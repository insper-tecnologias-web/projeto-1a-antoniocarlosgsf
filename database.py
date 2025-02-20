import sqlite3
from dataclasses import dataclass

class Database:
      def __init__(self, banco):
         self.conn = sqlite3.connect(f'{banco}.db')
         self.create_tabela()

      def create_tabela(self):
         query = """
         CREATE TABLE IF NOT EXISTS note(
            id INTEGER PRIMARY KEY,
            title TEXT,
            content TEXT NOT NULL
         );
         """
         cursor = self.conn.cursor()
         cursor.execute(query)
         self.conn.commit()

      def add(self, note):
         # query = """
         #    INSERT INTO note (title, content) VALUES ({note}.title, {note}.content)
         # """
         query = """
            INSERT INTO note (title, content) VALUES (?, ?)
         """
         cursor = self.conn.cursor()
         cursor.execute(query, (note.title, note.content))
         self.conn.commit()

      def get_all(self):
         cursor = self.conn.execute("SELECT id, title, content FROM note")
         notes = []
         for linha in cursor:
            identificador = linha[0]
            title = linha[1]
            content = linha[2]
            note = Note(id = identificador, title=title, content=content)
            notes.append(note)

         return notes

      def update(self, entry):
         print(entry)
         query = """
         UPDATE note SET title = ?, content = ? WHERE id = ?
         """
         cursor = self.conn.cursor()
         cursor.execute(query, (entry.title, entry.content, entry.id))
         self.conn.commit()

      def delete(self, note_id):
         query = """
         DELETE FROM note WHERE id = ?
         """
         cursor = self.conn.cursor()
         cursor.execute(query, (note_id,))
         self.conn.commit()

         

@dataclass
class Note:
   def __init__(self, id=None, title=None, content=''):
      self.id = id
      self.title = title
      self.content = content


   

      

