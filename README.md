# Evento

Problem Statement: Recieving lack of informations towards the college students about various fest,events,workshops,hackathons etc equally.
Solution:Design and develop a user friendly platform that allows users to browse through a diverse range of events,encompassing cultural festivals, technical symposiums, hackathons, workshops and seminars.



stack=html,css,python(flask)
login form
<form id="loginForm" action="/login" method="post">
    <label for="username">Username:</label>
    <input type="text" id="username" name="username" required><br><br>
    <label for="password">Password:</label>
    <input type="password" id="password" name="password" required><br><br>
    <button type="submit">Login</button>
</form>

choose your role form
<div>
    <p>Choose Your Role:</p>
    <input type="radio" id="organizer" name="role" value="organizer" required>
    <label for="organizer">Event Organizer</label><br>
    <input type="radio" id="participant" name="role" value="participant" required>
    <label for="participant">Event Participant</label><br>
</div>

css styling
<link rel="stylesheet" href="style.css">
<link rel="stylesheet" href="part.css">
