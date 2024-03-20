from PyQt5.QtCore import Qt, QEventLoop, QUrl
import rclpy
from rclpy.node import Node
from ament_index_python.packages import get_package_share_directory
import PyQt5
from PyQt5.QtWidgets import QSizePolicy, QApplication, QWidget, QPushButton, QVBoxLayout, QLabel, QMainWindow, QHBoxLayout, QListWidget, QListWidgetItem, QFileDialog,QCheckBox, QGridLayout
from PyQt5.QtMultimedia import QMediaContent, QMediaPlayer
from PyQt5.QtMultimediaWidgets import QVideoWidget
import sys
from std_msgs.msg import Bool, String 
from PyQt5.QtGui import QPixmap
import json
import os



class DesignChallenge3(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        
        self.setWindowTitle("Design Challenge #3")
        self.button = QPushButton("Add plants")
        self.button.setCheckable(True)
        self.label = QLabel()      
        #media player instance None, QMediaPlayer.VideoSurface
        # self.player = QMediaPlayer(None, QMediaPlayer.VideoSurface)
        horiz_layout = QHBoxLayout()   
        self.plants = ['Apple','Apricot','Avocado','Banana','Blackberry','Blueberry','Boysenberry','Cantaloupe','Cherry','Clementine','Coconut','Cranberry','Date','Dragonfruit','Elderberry','Fig','Grape','Grapefruit','Guava','Honeydew','Kiwi','Kumquat','Lemon','Lime','Lychee','Mango','Mulberry','Nectarine','Orange','Papaya','Passion Fruit','Peach','Pear','Pineapple','Plum','Pomegranate','Raspberry','Red Currant','Starfruit','Strawberry','Tangerine','Ugli Fruit','Watermelon','White Currant','White Sapote','Yellow Watermelon','Yuzu','Zucchini (Courgette)','Quince','Persimmon','Artichoke','Arugula','Asparagus','Beetroot','Bell Pepper','Black-eyed Peas','Broccoli','Brussels Sprouts','Cabbage','Carrot','Cauliflower','Celery','Chard','Collards','Corn','Cucumber','Eggplant','Fennel','Garlic','Green Beans','Kale','Leek','Lettuce','Mushroom','Mustard Greens','Okra','Onion','Parsnip','Pea','Potato','Pumpkin','Radish','Rhubarb','Rutabaga','Spinach','Squash','Sweet Potato','Tomato','Turnip','Watercress','Yam','Zucchini','Acorn Squash','Butternut Squash','Chayote','Chicory','Daikon','Endive','Kohlrabi','Parsley Root',]
        self.checkboxes = []

        
        grid_layout = QGridLayout()
        rows = 10  # adjust this value to your needs
        cols = 10  # adjust this value to your needs

        for i, plant in enumerate(self.plants):
            row = i // cols
            col = i % cols
            cb = QCheckBox(plant, self)
            grid_layout.addWidget(cb, row, col)
            self.checkboxes.append(cb)

        btn = QPushButton('Save', self)
        btn.clicked.connect(self.get_plants)

        self.main_pane = QVBoxLayout()
        grid_layout.addWidget(self.label)
        grid_layout.addWidget(self.button)

        horiz_layout.addLayout(grid_layout)
        horiz_layout.addLayout(self.main_pane)

        container = QWidget()
        container.setLayout(horiz_layout)
        self.setCentralWidget(container)
        self.showMaximized()
        self.show()

    # def promoVid(self,main_pane):
    #     pixmap = QPixmap('Logo_MainGreenBorder.png')
    #     self.label.setPixmap(pixmap)
    #     self.resize(pixmap.width(), pixmap.height())
    #     self.main_pane.addWidget(self.label)
    
    def get_plants(self):
        selected_plants = [cb.text() for cb in self.checkboxes if cb.isChecked()]
        self.create_json_parameter_file(selected_plants)# replace this with your saving logic

    

    def create_json_parameter_file(self,plant_name):
        #for each plant, create a json file with the parameters and add it to the dictionary
        read_filepath = "../parameters/plant_parameters.json"
        save_filepath = "../parameters/plants_in_pot_parameters.json"
        plant_parameters = json.load(open(read_filepath))
        if not os.path.exists(save_filepath):
            pot_parameters = []
            for plant in plant_name:
                parameters = { plant : plant_parameters[plant] }
                pot_parameters.append(parameters)
        with open(save_filepath, "w") as file:
            file.write(json.dumps(pot_parameters))

        
    # Define a method to handle errors
    def handleError(self, error):
        print("Error:", error)

    # def promoVid2(self):
    #     # fileName,_ = QFileDialog.getOpenFileName(self, ".","Images (*.mp4) (*.avi) (*.png)")
    #     fileName = get_package_share_directory('grr_guis') + '/multimedia/grr_logo.mp4'
    #     print(fileName)
    #     # if fileName != '':
    #     content = QUrl.fromLocalFile(fileName)    
    #     print(content)              
    #     self.player.setMedia(QMediaContent(content))
    #     self.player.play()
        
    
class Gui(Node):
    def __init__(self, application:QApplication, window:DesignChallenge3) -> None:
        super().__init__("GUI")
        self.start_button_pub = self.create_publisher(Bool, "/gui/start", 10)
        self.test_label = self.create_subscription(String, "/gui/info", self.display_test, 10)
        self.gui_loop_timer = self.create_timer(.1, self.gui_loop)
        self.app = application
        self.window = window
        self.previous_nodes = []
        self.bind()
        
    def bind(self):
        self.window.button.clicked.connect(self.save)
        
    def save(self, checked):
        self.window.get_plants()
        
    def run_video(self, msg:Bool):
        if msg.data:
            self.window.promoVid2()
    
    def display_test(self, msg:String):
        print(msg)
        self.window.label.setText(msg.data)
        
    def gui_loop(self):
        self.app.processEvents(flags=QEventLoop.ProcessEventsFlag.AllEvents)     
        # self.window.show()
            

def main():
    # create application instance
    app = QApplication([])
    #instance of widget
    window = DesignChallenge3()
    rclpy.init()
    gui = Gui(app, window)
    rclpy.spin(gui)




if __name__ == "__main__":
    main()