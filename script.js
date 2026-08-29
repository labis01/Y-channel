const STORAGE_KEY = 'y-channel-stories';

const form = document.getElementById('story-form');
const idField = document.getElementById('story-id');
const titleField = document.getElementById('story-title');
const tagsField = document.getElementById('story-tags');
const bodyField = document.getElementById('story-body');
const listEl = document.getElementById('story-list');
const emptyMessage = document.getElementById('empty-message');
const newBtn = document.getElementById('new-btn');

function loadStories() {
  try {
    return JSON.parse(localStorage.getItem(STORAGE_KEY)) || [];
  } catch {
    return [];
  }
}

function saveStories(stories) {
  localStorage.setItem(STORAGE_KEY, JSON.stringify(stories));
}

function resetForm() {
  form.reset();
  idField.value = '';
}

function parseTags(raw) {
  return raw
    .split(',')
    .map(t => t.trim())
    .filter(Boolean);
}

function renderStories() {
  const stories = loadStories();
  listEl.innerHTML = '';
  emptyMessage.hidden = stories.length > 0;

  stories
    .slice()
    .sort((a, b) => b.updatedAt - a.updatedAt)
    .forEach(story => {
      const li = document.createElement('li');
      li.className = 'story-card';

      const title = document.createElement('h3');
      title.textContent = story.title;

      const tags = document.createElement('div');
      tags.className = 'tags';
      tags.textContent = story.tags.length ? story.tags.join(', ') : '';

      const excerpt = document.createElement('p');
      excerpt.className = 'excerpt';
      excerpt.textContent = story.body.length > 160
        ? story.body.slice(0, 160) + '…'
        : story.body;

      const actions = document.createElement('div');
      actions.className = 'card-actions';

      const editBtn = document.createElement('button');
      editBtn.textContent = 'Edit';
      editBtn.addEventListener('click', () => {
        idField.value = story.id;
        titleField.value = story.title;
        tagsField.value = story.tags.join(', ');
        bodyField.value = story.body;
        titleField.focus();
        window.scrollTo({ top: 0, behavior: 'smooth' });
      });

      const deleteBtn = document.createElement('button');
      deleteBtn.textContent = 'Delete';
      deleteBtn.className = 'delete';
      deleteBtn.addEventListener('click', () => {
        const remaining = loadStories().filter(s => s.id !== story.id);
        saveStories(remaining);
        if (idField.value === story.id) resetForm();
        renderStories();
      });

      actions.append(editBtn, deleteBtn);
      li.append(title, tags, excerpt, actions);
      listEl.appendChild(li);
    });
}

form.addEventListener('submit', e => {
  e.preventDefault();

  const stories = loadStories();
  const now = Date.now();
  const title = titleField.value.trim() || 'Untitled story';
  const tags = parseTags(tagsField.value);
  const body = bodyField.value;

  if (idField.value) {
    const story = stories.find(s => s.id === idField.value);
    if (story) {
      story.title = title;
      story.tags = tags;
      story.body = body;
      story.updatedAt = now;
    }
  } else {
    stories.push({
      id: crypto.randomUUID(),
      title,
      tags,
      body,
      createdAt: now,
      updatedAt: now,
    });
  }

  saveStories(stories);
  resetForm();
  renderStories();
});

newBtn.addEventListener('click', resetForm);

renderStories();
