from dbload import load_counties, load_states, start_session
import numpy as np

session = start_session("sqlite:///database.sqlite")
data_counties = load_counties(session, filter_empty=True)
counties_mat = np.array(list(map(lambda x:x.get_vector().numerical(), data_counties)))

loser_states_dem = []
loser_states_rep = []

data_states = load_states(session)
states_mat = np.array(list(map(lambda x:x.get_vector().numerical(), data_states)))
states_labels = np.array(list(map(lambda x:x.get_vector().labels(), data_states)))

print(data_states)
loser_states_dem = ['Colorado', 'Hawaii', 'Idaho', 'Illinois', 'Indiana', 'Michigan', 'Montana', 'Nebraska', 'Oklahoma', 'Oregon', 'Utah', 'Washington', 'West Virginia', 'Wisconsin', 'Wyoming']
loser_states_rep = ['Idaho', 'Iowa', 'Ohio', 'Oklahoma', 'Texas', 'Utah', 'Wisconsin']

#finding loser democratic and republican states
# for state in data_states:
#     print(state)
#     if state.democrat.votes and state.democrat.votes['Bernie Sanders']>state.democrat.votes['Hillary Clinton']:
#         loser_states_dem.append(state)
#     if state.republican.votes:
#         max_votes_rep = max(state.republican.votes.values())
#         print(max_votes_rep)
#         winner = list(filter(lambda x: x[1] == max_votes_rep, state.republican.votes.items()))[0]
#         if winner[0] != 'Donald Trump':
#             loser_states_rep.append(state)

# print('all: ', len(data_states))
#print('loser rep: ', len(loser_states_rep))
