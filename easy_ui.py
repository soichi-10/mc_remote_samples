import tkinter as tk
import threading

class MultiNumericUI:
    def __init__(self, title, items, buttons):
        self.title = title   # 【修正】受け取った名前を保存する
        self.values = items
        self.buttons = buttons
        self.labels = {}
        threading.Thread(target=self._build_ui, daemon=True).start()

    def _build_ui(self):
        root = tk.Tk()
        root.title(self.title) # 【修正】"ui" ではなく self.title を使う
        root.attributes("-topmost", True)

        # 辞書の中身をすべて入力欄にする
        for name, val in self.values.items():
            frame = tk.LabelFrame(root, text=name, padx=10, pady=2)
            frame.pack(padx=20, pady=2, fill=tk.X)
            var_str = tk.StringVar(value=str(val))
            self.labels[name] = var_str

            def make_change(n, d):
                def c():
                    self.values[n] += d
                    self.labels[n].set(str(self.values[n]))
                return c

            tk.Button(frame, text="◀", command=make_change(name, -1), width=5).pack(side=tk.LEFT)
            tk.Label(frame, textvariable=var_str, width=10, bg="white").pack(side=tk.LEFT, padx=10)
            tk.Button(frame, text="▶", command=make_change(name, 1), width=5).pack(side=tk.LEFT)

        # ボタンエリア
        for btn_name, func in self.buttons.items():
            def trigger(f=func):
                # ボタンを押した時に現在の値のコピーを渡して実行
                threading.Thread(target=f, args=(self.values.copy(),), daemon=True).start()
            
            tk.Button(root, text=btn_name, command=trigger, height=2,
                      bg="#f0f0f0").pack(pady=5, fill=tk.X, padx=20)

        root.mainloop()