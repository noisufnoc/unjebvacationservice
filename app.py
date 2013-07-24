#!/usr/bin/env python
import random
from flask import Flask, jsonify

app = Flask(__name__)


facts = [
    'On March 1, 1803, Ohio became the 17th state of the Union.',
    'Ohio is also known as the Buckeye State.',
    'The official state rock song Hang On Sloopy.',
    'Ohio is the leading producer of nursery & greenhouse plants.',
    'Ohio has an area of 116,103 sq miles. It ranks 34th in state size.',
    'Ohio is the only state where its state flag is of a pennant design.',
    'Founded in 1788 by General Rufus Putnam, Marietta - named after the then Queen of France Marie Antoinette - was \
    Ohio\'s first permanent settlement.',
    'Columbus is Ohio\'s state capital (even though Chillicothe was the 1st) & largest city.',
    'Did you know that half of the US population lives within a 500 mile radius of the city of Columbus?',
    'In 1899, the first full time automobile service station was opened here in Ohio.',
    '7 US presidents were born in Ohio, being: Ulysses S. Grant, Rutherford B. Hayes, James Garfield, Benjamin \
    Harrison, William McKinley, William H. Taft, and Warren G. Harding..',
    'The automobile self-starter was invented by Charles Kettering of Loundonville in 1911.',
    'The first hot dog was created in Ohio by Harry M. Stevens in 1900.',
    'Teflon was was invented by Roy J. Plunkett of New Carlisle in 1938.',
    'The world\'s largest basket is located in Dresden Ohio at Basket Village USA.',
    'Chewing gum was patented by W.F. Semple of Mount Vernon Ohio in 1869.',
    'In 1869, The Cincinnati Red Stockings became the first professional baseball team.',
    'On the north side of Kelleys Island in Ohio, The Glacial Grooves on the north side of Kelleys Island - scoured \
    into solid limestone bedrock about 18,000 years ago by the great ice sheet - are the largest easily accessible \
    glacial grooves in the world.',
    'Well-known personalities from Ohio include: Steven Spielberg, Drew Carey, Annie Oakley, \
    Paul Newman, Arsenio Hall & Clark Gable.',
    'Fostoria is the The only city in Ohio that is situated in 3 counties (Hancock, Seneca & Wood).',
    'A famous earthen mound in the shape of a serpent near Peebles Ohio, Serpent Mound State Memorial, winds along for \
    a total length of 411 m (1348 ft).',
    'The famous inventor from Milan Ohio, Thomas Edison, invented or developed the incandescent light bulb, \
    phonograph, and the early motion picture camera.',
    'The United States Public Land Survey Ordinance of 1785 - providing the administration and subdivision of land \
    in the Old Northwest Territory, was first enacted from the starting point of East Liverpool in Ohio. \
    From this starting point, this ectangular-grid land survey divided all public lands into townships \
    six mile squares.',
    'Cincinnati was the home of the first professional city fire department.',
    'As a solution to halting the pilfering of his profits by patrons, James J. Ritty, of Dayton Ohio,\
    invented the cash register in 1879.',
    'Neil Armstrong of Wapakoneta Ohio, became the first man to walk on the moon.',
    'La Rue, Ohio was the home of the first gasoline powered fire engine.',
    'In 1891, John Lambert of Ohio City made America\'s first automobile, though was unable to sell one.',
    'The Winton Motor Carriage Company ,founded in Cleveland Ohio in 1897,\
    was one of the first American companies to sell a motor car.',
    'Ohio Automobile Company (later to be called the Packard Motor Car Company) was founded in Warren Ohio\
    in 1900, to compete with the product manufactured by The Winton Motor Carriage Company.',
    'The Wright Brothers from Dayton are credited as inventors of the first gasoline powered airplane.',
    'In 2008, Cleveland ranked 7th as the most dangerous city in the US among cities with a population of \
    100,000 to 500,000 and the 11th most dangerous overall.'
]


@app.route('/')
def index():
    return jsonify({'fact': facts[random.randint(0, (len(facts)-1))]})


if __name__ == '__main__':
    app.run()

