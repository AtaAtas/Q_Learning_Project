#bu kod tamamen suttonun value iterationdaki psüdokodu üzerine inşa edilmiş
#ve aynı kitaptaki gambler's problem isimli örneği koda dökmeyi amaçlamıştır.
import numpy as np

head_prob = 0.4
the_last_state = 100
the_first_state = 0
theta = 0.00001 #tamamiyle salladım

def set_up_enviorement():
    states = np.arange(0, 101)
    return states

def possible_actions(s):
    action_list = np.arange(1,min(s, the_last_state - s) + 1)
    return action_list

def get_reward(s):
    if s != the_last_state:
        return +1
    return 0

def state_value_func():
    states = set_up_enviorement()
    v = np.zeros(the_last_state+1)
    v[the_last_state] = 1  # for reward other ones are 0 according to sutton book
    #print(v)
    
    for _ in range(10001):
        delta = 0

        for state in states[1:the_last_state]: #the first and the last are terminal states
            actions = possible_actions(state)
            max_value = 0
            
            for a in actions:
                q_value = head_prob * (get_reward(state+a)+v[state + a]) + (1 - head_prob) *(get_reward(state-a) + v[state - a]) # aslında +1 olması gerekirdi ancak örneğin yazı gelirse
                #kumarbaza a kadar para kazandırıcak ve state + a kadar sonraki duruma atacak dolayısı ile oranın beklenen değerini almış olacak
                # ve aynı mantıkla tura geldiğinde a kadar para kaybedeck
                max_value = max(max_value, q_value)
                #print(max_value)

            delta = max(delta, abs(max_value - v[state]))
            #print(delta)
            v[state] = max_value

            if delta < theta:
                break
            

    return v


def optimal_policy(v):
    policy = np.zeros(the_last_state + 1)
    enviorenment = set_up_enviorement()[1:the_last_state]
    for state in enviorenment: 
        actions = possible_actions(state)
        best_action = 0
        best_value = 0
        #print(state)
        for a in actions:
            q_value = (head_prob * (get_reward(state + a) + v[state + a]) + (1 - head_prob) * (get_reward(state - a) + v[state - a]))

            if q_value > best_value:
                best_value = q_value
                best_action = a
            #print(best_action)
        policy[state] = best_action  
    print(policy)
    return policy

v = state_value_func()
policy = optimal_policy(v)

print("Optimal Value Function:")
print(v)

print("\nOptimal Policy:")
print(policy)
