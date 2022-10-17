# Instructor Training Curriculum Maintainance

This document describes how the Carpentries Community maintains the Instructor Training (IT) Curriculum.  
Because this curriculum is taught by a select group of individuals and serves as an entrypoint for 
instructors who teach other curricula for The Carpentries, maintainance of the IT curriculum involves
a greater number of stakeholders.  

The IT curriculum does not have a standard Curriculum Advisory Committee. Instead the Trainers Leadership Committee
fulfills this role and solicits feedback from the whole community of trainers as needed. 

## Definitions 

**Patches** are typo fixes and in situ rearticulations of paragraphs to improve clarity. There's no change in lesson or in-episode order and there is no expectation that notice needs to be given to trainers preparing to run a workshop. 

**Minor updates** are PRs from issues that make changes to a single conceptual component of the curriculum, even if it addresses multiple issues to multiple sections of the curriculum. These changes may require a change to how a trainer prepares to teach, but do not substantially change key points or the order of materials. 

**Major updates** are updates that make multiple conceptual changes or change the key points of episodes. This includes PRs that resolve multiple interdependent issues; represent significant changes in terminology or framing; change which topics are covered or substantially reorder material. 

## Role of Maintainers 

- perform routine maintenance duties as [outlined by the Maintainer community](https://carpentries.github.io/maintainer-onboarding/05-communicate-advisors/index.html)
- refer issues to Trainer community for discussion
- provide peer review during major updates (see below)
- recruit and delegate to individuals or focus groups to collaborate on specific topics or tasks of interest
- complete certification as a Carpentries Maintainer as possible and practical

PR Handling:
- Patches may be merged by any maintainer without discussion. 
- Minor changes can be merged by any maintainer who did not contribute to the PR, after approval by another trainer, or after discussion among maintainers.
- PRs for major changes or that impact policy are described in the special sections below. 

## Maintainer Selection

This group should consist of at least 3 people:
- 1 designated member of The Carpentries Core Team
- 1 member of the Trainers Leadership Committee
- 1 additional Trainer

At least one member of this group should be certified as a Carpentries Maintainer, trainers
may be appointed prior to certification, but must take steps to complete that certification
upon appointment.  The Trainers Leadership Committee shall approve appointments to the maintainer 
committee each year. Additional maintainers may be added at any time by recommendation of
the existing maintainers with approval of the Trainers Leadership Committee. 

## Special Maintance Procedures/Sections

### Major Updates and Releases

To initiate a major update, the maintainers will submit a proposal for approval to the Trainers Leadership Committee. 
  - technical workflow (after consultation with the Core Team Infrastructure team)
  - scope
  - timeline for notifiying the trainer community at large
  - how the process addressess challenges faced in previous major updates

The process must include, but is not limited to:
  - time for pilot teaching by trainers that are not maintainers, members of the Trainers Leadership Committee, or Core Team
  - at least two weeks of asynchronous feedback with notifications for all trainers

Before a major update is merged, the maintainers submit a proposal to the Trainers Leadership Committee that describes:
  - a summary of changes
  - the completed opportunities for community feedback
  - opportunities to improve the major update process for next time.  

After a major update, a release will be issued in collaboration with the Core Team Infrastructure Team. 
  
### Policy and Starting Points for Teaching Demonstrations

Some parts of the Instructor Training Curriculum cover policy, both Instructor Training and 
general Carpentries Policy. General Policy changes that impact IT Curriculum will have PRs 
submitted by the Core Team. 

Instructor training related procedure and policy will go through the Trainers Leadership Committee. 
The PR to the curriculum repository should be linked to a proposal by that group linking the Trainers Leadership Committee
approval to these changes. 

The "Suggested Lessons for Teaching Demonstrations" page will be maintained by the Curriculum team. 
Approved starting points shall be at the start of an episode and avoid dependencies. 
Recommended changes to this page will be referred to the curriculum team for approval. 
Proposals for new starting points in issues will be tagged by the maintainers for consideration by this group. 

When a new official curriculum is introduced, the Curriculum Team will prepare a list of starting points to be added.
In this circumstance, a member of the Curriculum Team will open a pull request to add the new starting points and tag the Instructor Training Maintenance Team for review and approval.

### Using Trainer Meetings 

Any instructor trainer may ask for a pause on a Pull Request if they think it deserves discussion at the next meeting. After the next meeting, the pause is immediately dropped unless there are strong reasons to the contrary.

## Approval and Ratification

This policy may be updated by approval of the Trainers Leadership Committee after a two week comment period by the trainer community at large. 
  
