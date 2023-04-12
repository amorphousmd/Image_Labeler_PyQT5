from PyQt5.QtGui import QPixmap, QPainter, QPen
from PyQt5.QtWidgets import QApplication, QLabel, QGraphicsScene, QGraphicsView, QGraphicsRectItem
from PyQt5.QtCore import Qt, QRectF

class AnnotationView(QGraphicsView):
    def __init__(self, pixmap):
        super().__init__()
        self.scene = QGraphicsScene()
        self.setScene(self.scene)
        self.rect_item = QGraphicsRectItem()
        self.rect_item.setPen(QPen(Qt.red, 2))
        self.rect_item.setVisible(False)
        self.scene.addItem(self.rect_item)
        self.setDragMode(QGraphicsView.ScrollHandDrag)
        self.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.setRenderHint(QPainter.Antialiasing)
        self.setRenderHint(QPainter.SmoothPixmapTransform)
        self.setSceneRect(QRectF(pixmap.rect()))
        self.setFixedSize(pixmap.width(), pixmap.height())
        self.setBackgroundBrush(pixmap)

    def mousePressEvent(self, event):
        super().mousePressEvent(event)
        self.rect_item.setRect(event.scenePos().x(), event.scenePos().y(), 0, 0)
        self.rect_item.setVisible(True)

    def mouseMoveEvent(self, event):
        super().mouseMoveEvent(event)
        rect = QRectF(self.rect_item.rect().topLeft(), event.scenePos())
        self.rect_item.setRect(rect.normalized())

# Load the image
image = QPixmap('image.jpg')

# Create the annotation view and show it
app = QApplication([])
view = AnnotationView(image)
view.show()
app.exec_()
