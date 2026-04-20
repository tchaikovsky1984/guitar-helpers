import { useState } from 'react'
import './App.css'

function App() {
  const [sharps, setSharps] = useState(true);
  const [time, setTime] = useState(1);
  const [note, setNote] = useState("E");

  let notes: string[] = ['A', 'A#', 'B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#'];

  const handleCheckboxChange = () => {
    setSharps(!sharps);
  };
  const handleNumberChange = (e) => {
    const target = e.target;
    const value = target.value;
    setTime(value);
  };

  async function startLoop(e) {
    e.preventDefault();
    let currentNotes = [...notes];
    if (!sharps) {
      currentNotes = currentNotes.filter((note) => note.length === 1);
    }
    while (true) {
      const randomIdx = Math.floor(Math.random() * currentNotes.length);
      setNote(currentNotes[randomIdx]);
      await new Promise(resolve => setTimeout(resolve, time * 1000));
    }
  }

  return (
    <>
      <section id='center'>
        <div>
          <h1>Note Helper</h1>
          <form style={{ display: 'flex', flexDirection: 'column', gap: '15px', alignItems: 'center' }}>
            <div style={{ display: 'flex', flexDirection: 'column', alignItems: 'center' }}>
              <label htmlFor="sharps">Include Sharps?:</label>
              <input
                id="sharps"
                type='checkbox'
                name='sharps'
                checked={sharps}
                onChange={handleCheckboxChange}
              />
            </div>

            <div style={{ display: 'flex', flexDirection: 'column', alignItems: 'center' }}>
              <label htmlFor="time">Time Between Prompts (s):</label>
              <input
                id="time"
                type='number'
                name='time'
                value={time}
                onChange={handleNumberChange}
              />
            </div>

            <button onClick={startLoop}>Start</button>
          </form>
        </div>
        <div style={{ marginTop: '40px' }}>
          <h2 style={{ fontSize: '4rem' }}>{note}</h2>
        </div>
      </section>
    </>
  );
}

export default App
