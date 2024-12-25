import tkinter as tk
from tkinter import messagebox
from copy import deepcopy

def SLAY(matrix):
    n = len(matrix)
    b = [matrix[i][-1] for i in range(n)]
    A = [row[:-1] for row in matrix]

    def opredelitel(mat):
        if len(mat) == 1:
            return mat[0][0]
        if len(mat) == 2:
            return mat[0][0] * mat[1][1] - mat[0][1] * mat[1][0]
        determinant = 0
        for c in range(len(mat)):
            minor = [row[:c] + row[c + 1:] for row in mat[1:]]
            determinant += ((-1) ** c) * mat[0][c] * opredelitel(minor)
        return determinant

    opr_A = opredelitel(A)
    if opr_A == 0:
        return "Система не имеет единственного решения"

    solutions = []
    for i in range(n):
        temp_A = deepcopy(A)
        for j in range(n):
            temp_A[j][i] = b[j]
        sol = opredelitel(temp_A) / opr_A
        solutions.append(sol)

    return solutions

def on_submit():
    try:
        rows = int(entry_rows.get())
        columns = int(entry_columns.get())
        if columns < 2:
            raise ValueError("Количество столбцов должно быть больше 1")

        matrix = []
        for i in range(rows):
            row = list(map(float, entry_matrix[i].get().split()))
            if len(row) != columns:
                raise ValueError("Количество коэффициентов в строке должно соответствовать размеру матрицы")
            matrix.append(row)

        result = SLAY(matrix)
        messagebox.showinfo("Решение", f"Решение: {result}")
    except Exception as e:
        messagebox.showerror("Ошибка", str(e))

entry_matrix = []

def create_matrix_inputs(rows, columns):
    global entry_matrix
    for widget in matrix_frame.winfo_children():
        widget.destroy()
    entry_matrix = []
    for i in range(rows):
        entry = tk.Entry(matrix_frame)
        entry.grid(row=i, column=0, columnspan=columns)
        entry_matrix.append(entry)

#main

root = tk.Tk()
root.geometry('300x250')
root.title("Решение СЛАУ от студента группы ВПР11 Александра Михайлова с помощью формулы Крамера")

tk.Label(root, text="Количество строк:").grid(row=0, column=0)
entry_rows = tk.Entry(root)
entry_rows.grid(row=0, column=1)

tk.Label(root, text="Количество столбцов:").grid(row=1, column=0)
entry_columns = tk.Entry(root)
entry_columns.grid(row=1, column=1)

btn = tk.Button(root, text="Создать поля ввода", command=lambda: create_matrix_inputs(int(entry_rows.get()), int(entry_columns.get())))
btn.grid(row=2, columnspan=2)

matrix_frame = tk.Frame(root)
matrix_frame.grid(row=3, columnspan=2)

submit_btn = tk.Button(root, text="Решить", command=on_submit)
submit_btn.grid(row=4, columnspan=2)

root.mainloop()