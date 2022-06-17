This directory is used to render the html pages.It is basically used for templates.
Jo bhi ham templates daalte hain is directory mein usko ham rendertemplate function ka use karke 
apni website par render kara skte hain

Bootstrap hamari wo library jis par pehle se hi kisi ne website nbanakarke rakhi hai har ek zaroorat ko dhyaan 
mein rakhte huye ham bas wahi code uthakar ke copy paste kar skte hain agar hame frontr end ki tension nahi leni hai
aur khud se nhi design karni hai website to.

JINJA2 hamara ek templating engine hota hai jiska ki ham tab use karte hain jab ham koi flask app banate hain
aur koi python ka variable bhej detein hain apni app.py file se taaki ham us variable ko apne html page par render 
kara skein to jinja 2 ek way pave karta hai python aur html ke beech mein variable ke aadan pradaan ka.
Jahan par rendertemplate function lagaya hoga usi mein ham saath mein ek variable kar denge aur wo variable phir
hamare python se html par available ho jaayega aur ham ushe easily use kar paayenge.  

<!--0 yellow  1 red 2 green 3 blue
{% if loop.index0 is divisibleby 4%}                    
{%set i=0%}
{%else%}
{%set i= loop.index0%4 %}
{%endif%}-->

{% if alltodo|length %} isme length jo hai ek filter ki tarah act kar raha hai jinja2 ka agar length jo hai alltodo ki wo kx
nhi hai tab ham show kar rahe hain coontent ki add your first todo
agar length kx hai alltodo ki to ham simply un todos ko table ke format mein print kar denge

Template Inheritance in jinja2
Ek jagah ham kisi ek html ke element ko rakhkar ke alag alag jagah par use change kar skte hain by using inheritance 
of templates maan lo hamarae pass 100 html pages hain aur un 100 pages ko hame design karna hai same website ke
to ek basic structure ham bana ke apne page ka use baaki saare pages mein inherit kara lenge jis se ki hame baar 
baar ek hi cheez nahi likhni padegi.(jaise ki ham yahan par bana rahe hain base.html template banaya phir use
update.html aur index.html dono mein hi extend kara wa diya aur jo block hamne create kiya the base mein use in 
dono template mein jo code different us se fill kara diya)
1 hour 20 minute full_work_flow