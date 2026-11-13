from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QLineEdit, QComboBox, QPushButton, QMessageBox
import sys


def the_button_clicked():
    text_out = text_writing.text()

    if text_out.strip() == '' :
        label2.setText('firstly add your answer')
        QMessageBox.warning(window, 'CRITICAL CONDITION', 'why dont you want to talk?')
        return
    text_out = float(text_out)
    
    text_list_out = the_list.currentText()

    if text_list_out == 'i am good today':
        if text_out <= 7:
            label2.setText('good day, get to bed early tonight')
        else:
            label2.setText('you can anything today!')
    elif text_list_out == 'i am feel sadness':
        if text_out <= 7:
            label2.setText('go to sleep right now')
        else:
            label2.setText('what happened? ;(')
    elif text_list_out == 'i am happy' :
        if text_out <= 7:
            label2.setText('thats great but start change your sleep habbits')
        else:
            label2.setText('i envy you!!!')
        
    
    

    


app = QApplication(sys.argv)

window = QWidget()
window.setWindowTitle('good morning !')

label = QLabel("how did you sleep today?: ", window)

text_writing = QLineEdit()
text_writing.setPlaceholderText('add hours number')

the_list = QComboBox()
the_list.addItems(['i am good today', 'i am feel sadness', 'i am happy'])

the_button = QPushButton('I AM READY')

label2 = QLabel("", window)

compaine1 = QVBoxLayout()
compaine1.addWidget(label)
compaine1.addWidget(text_writing)
compaine1.addWidget(the_list)
compaine1.addWidget(the_button)
compaine1.addWidget(label2)
window.setLayout(compaine1)

the_button.clicked.connect(the_button_clicked)

window.show()
app.exec()